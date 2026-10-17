#!/usr/bin/env python3
"""Static risk inventory for WeChat Official Account article source packages."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import tempfile
import zipfile
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


RISK_TAGS = {
    "script": ("阻断", "JavaScript runtime"),
    "iframe": ("阻断", "iframe content"),
    "form": ("阻断", "form submission"),
    "input": ("高", "form control"),
    "select": ("高", "form control"),
    "textarea": ("高", "form control"),
    "button": ("高", "button requiring browser behavior"),
    "canvas": ("阻断", "canvas runtime"),
    "object": ("阻断", "embedded object"),
    "embed": ("阻断", "embedded content"),
    "video": ("中", "native or imported video"),
    "audio": ("中", "native or imported audio"),
    "svg": ("中", "inline SVG"),
    "animate": ("高", "SVG animation"),
    "animatetransform": ("高", "SVG animation"),
    "foreignobject": ("高", "SVG foreignObject"),
}

CSS_RULES = [
    ("CSS_ANIMATION", "高", re.compile(r"(?:@keyframes|\banimation(?:-\w+)?\s*:)", re.I), "CSS animation"),
    ("CSS_TRANSITION", "中", re.compile(r"\btransition(?:-\w+)?\s*:", re.I), "CSS transition"),
    ("CSS_HOVER", "高", re.compile(r":hover\b", re.I), "hover-only selector"),
    ("CSS_FIXED_STICKY", "高", re.compile(r"position\s*:\s*(?:fixed|sticky)\b", re.I), "fixed or sticky positioning"),
    ("CSS_VIEWPORT", "中", re.compile(r"-?\d*\.?\d+(?:vh|vw|vmin|vmax)\b", re.I), "viewport-relative sizing"),
    ("CSS_NEGATIVE_MARGIN", "高", re.compile(r"margin(?:-(?:top|right|bottom|left))?\s*:\s*-", re.I), "negative margin or overlap"),
    ("CSS_GRID", "中", re.compile(r"display\s*:\s*(?:inline-)?grid\b", re.I), "CSS grid layout"),
    ("CSS_FILTER_MASK", "中", re.compile(r"(?:backdrop-filter|filter|mask(?:-\w+)?|clip-path)\s*:", re.I), "filter, mask, or clipping effect"),
    ("CSS_OVERFLOW", "中", re.compile(r"overflow(?:-x)?\s*:\s*(?:auto|scroll|hidden)\b", re.I), "overflow-dependent layout"),
]

REF_ATTRS = {"src", "srcset", "href", "poster", "xlink:href"}
ASSET_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".mp4", ".mov", ".mp3", ".m4a", ".wav", ".woff", ".woff2", ".ttf", ".otf", ".css", ".js"}
CSS_URL_RE = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.I)


class SourceParser(HTMLParser):
    def __init__(self, source: Path):
        super().__init__(convert_charrefs=True)
        self.source = source
        self.findings: list[dict] = []
        self.refs: list[dict] = []
        self.css_chunks: list[tuple[int, str]] = []
        self._in_style = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]):
        self._handle_tag(tag, attrs)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]):
        self._handle_tag(tag, attrs)

    def handle_endtag(self, tag: str):
        if tag.lower() == "style":
            self._in_style = False

    def handle_data(self, data: str):
        if self._in_style and data.strip():
            self.css_chunks.append((self.getpos()[0], data))

    def _handle_tag(self, tag: str, attrs: list[tuple[str, str | None]]):
        tag_lower = tag.lower()
        line = self.getpos()[0]
        if tag_lower == "style":
            self._in_style = True
        if tag_lower in RISK_TAGS:
            severity, reason = RISK_TAGS[tag_lower]
            self.findings.append(finding(f"TAG_{tag_lower.upper()}", severity, self.source, line, reason, f"<{tag}>"))
        for name, value in attrs:
            name_lower = name.lower()
            value = value or ""
            if name_lower.startswith("on"):
                self.findings.append(finding("EVENT_HANDLER", "blocker", self.source, line, "inline JavaScript event handler", name))
            if name_lower == "style":
                self.css_chunks.append((line, value))
            if name_lower in REF_ATTRS and value:
                values = [value]
                if name_lower == "srcset":
                    values = [item.strip().split()[0] for item in value.split(",") if item.strip()]
                for ref_value in values:
                    self.refs.append({"file": str(self.source), "line": line, "tag": tag_lower, "attribute": name_lower, "value": ref_value})


def finding(rule_id: str, severity: str, source: Path, line: int | None, message: str, evidence: str) -> dict:
    return {
        "rule_id": rule_id,
        "severity": severity,
        "file": str(source),
        "line": line,
        "message": message,
        "evidence": evidence[:240],
    }


def safe_extract(archive: Path, destination: Path) -> list[str]:
    rejected: list[str] = []
    root = destination.resolve()
    with zipfile.ZipFile(archive) as zf:
        for info in zf.infolist():
            target = (destination / info.filename).resolve()
            try:
                target.relative_to(root)
            except ValueError:
                rejected.append(info.filename)
                continue
            if info.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            with zf.open(info) as src, target.open("wb") as dst:
                shutil.copyfileobj(src, dst)
    return rejected


def image_metadata(path: Path) -> dict:
    data: dict = {"path": str(path), "type": path.suffix.lower(), "bytes": path.stat().st_size}
    try:
        from PIL import Image

        with Image.open(path) as img:
            data["width"], data["height"] = img.size
            data["format"] = img.format
            if getattr(img, "n_frames", 1) > 1:
                data["frames"] = img.n_frames
                duration = 0
                for index in range(img.n_frames):
                    img.seek(index)
                    duration += int(img.info.get("duration", 0))
                data["duration_ms"] = duration
    except Exception as exc:
        data["metadata_note"] = f"unreadable image metadata: {exc.__class__.__name__}"
    return data


def asset_metadata(path: Path) -> dict:
    if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp"}:
        return image_metadata(path)
    return {"path": str(path), "type": path.suffix.lower(), "bytes": path.stat().st_size}


def css_references(css: str, source: Path, start_line: int = 1) -> list[dict]:
    refs: list[dict] = []
    for match in CSS_URL_RE.finditer(css):
        value = match.group(2).strip()
        if not value:
            continue
        line = start_line + css.count("\n", 0, match.start())
        refs.append({"file": str(source), "line": line, "tag": "css", "attribute": "url", "value": value})
    return refs


def classify_ref(ref: dict, html_path: Path, root: Path) -> dict:
    value = ref["value"].strip()
    parsed = urlparse(value)
    result = dict(ref)
    is_destination = ref.get("tag") == "a" and ref.get("attribute") == "href"
    if value.startswith("data:"):
        result["kind"] = "embedded-data"
        return result
    if parsed.scheme in {"http", "https"} or value.startswith("//"):
        result["kind"] = "remote-destination" if is_destination else "remote"
        return result
    if parsed.scheme in {"mailto", "tel", "javascript", "weixin"}:
        result["kind"] = "destination-scheme" if is_destination else "scheme"
        return result
    if value.startswith("#"):
        result["kind"] = "fragment"
        return result
    clean = unquote(parsed.path).replace("\\", "/")
    candidate = (html_path.parent / clean).resolve()
    result["resolved"] = str(candidate)
    try:
        candidate.relative_to(root.resolve())
        if is_destination:
            result["kind"] = "local-destination"
        else:
            result["kind"] = "local" if candidate.exists() else "missing-local"
    except ValueError:
        result["kind"] = "outside-package"
    return result


def inspect_root(root: Path, rejected_zip_entries: list[str], only_html: Path | None = None) -> dict:
    html_files = [only_html] if only_html else sorted([p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in {".html", ".htm"}])
    findings: list[dict] = []
    refs: list[dict] = []
    for html_path in html_files:
        try:
            source = html_path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            findings.append(finding("READ_ERROR", "阻断", html_path, None, "unable to read HTML", str(exc)))
            continue
        parser = SourceParser(html_path)
        parser.feed(source)
        findings.extend(parser.findings)
        refs.extend(classify_ref(ref, html_path, root) for ref in parser.refs)
        for line, css in parser.css_chunks:
            refs.extend(classify_ref(ref, html_path, root) for ref in css_references(css, html_path, line))
            for rule_id, severity, pattern, message in CSS_RULES:
                match = pattern.search(css)
                if match:
                    findings.append(finding(rule_id, severity, html_path, line, message, match.group(0)))

    if only_html:
        css_files = sorted({Path(ref["resolved"]) for ref in refs if ref["kind"] == "local" and Path(ref["resolved"]).suffix.lower() == ".css"})
    else:
        css_files = sorted([p for p in root.rglob("*.css") if p.is_file()])
    for css_path in css_files:
        css = css_path.read_text(encoding="utf-8", errors="replace")
        refs.extend(classify_ref(ref, css_path, root) for ref in css_references(css, css_path))
        for rule_id, severity, pattern, message in CSS_RULES:
            match = pattern.search(css)
            if match:
                line = 1 + css.count("\n", 0, match.start())
                findings.append(finding(rule_id, severity, css_path, line, message, match.group(0)))

    for ref in refs:
        if ref["kind"] == "missing-local":
            findings.append(finding("MISSING_LOCAL_ASSET", "阻断", Path(ref["file"]), ref["line"], "missing local reference", ref["value"]))
        elif ref["kind"] == "outside-package":
            findings.append(finding("OUTSIDE_PACKAGE_ASSET", "高", Path(ref["file"]), ref["line"], "reference resolves outside package", ref["value"]))
        elif ref["kind"] == "remote":
            findings.append(finding("REMOTE_DEPENDENCY", "高", Path(ref["file"]), ref["line"], "remote dependency requires final-route transfer proof", ref["value"]))
        elif ref["kind"] == "remote-destination":
            findings.append(finding("EXTERNAL_DESTINATION", "中", Path(ref["file"]), ref["line"], "external destination requires permission and route testing", ref["value"]))
        elif ref["kind"] == "local-destination":
            findings.append(finding("LOCAL_DESTINATION", "高", Path(ref["file"]), ref["line"], "local document destination will not transfer as an article link", ref["value"]))
        elif ref["kind"] in {"scheme", "destination-scheme"} and ref["value"].lower().startswith("javascript:"):
            findings.append(finding("JAVASCRIPT_URL", "阻断", Path(ref["file"]), ref["line"], "javascript URL", ref["value"]))
        elif ref["kind"] == "destination-scheme":
            findings.append(finding("DESTINATION_SCHEME", "中", Path(ref["file"]), ref["line"], "destination scheme requires client testing", ref["value"]))

    for name in rejected_zip_entries:
        findings.append(finding("ZIP_PATH_TRAVERSAL", "阻断", root, None, "unsafe ZIP entry rejected", name))

    assets = sorted(asset_metadata(p) for p in root.rglob("*") if p.is_file() and p.suffix.lower() in ASSET_EXTS)
    counts = Counter(item["severity"] for item in findings)
    return {
        "root": str(root),
        "html_files": [str(p) for p in html_files],
        "summary": {
            "html_files": len(html_files),
            "assets": len(assets),
            "references": len(refs),
            "remote_dependencies": sum(1 for r in refs if r["kind"] == "remote"),
            "external_destinations": sum(1 for r in refs if r["kind"] == "remote-destination"),
            "missing_local_assets": sum(1 for r in refs if r["kind"] == "missing-local"),
            "findings_by_severity": dict(sorted(counts.items())),
        },
        "findings": findings,
        "references": refs,
        "assets": assets,
        "limitations": [
            "Static inspection does not reproduce WeChat sanitization.",
            "A clean report does not prove editor survival or device compatibility.",
            "Current platform limits and account permissions require E2 or E3 evidence.",
        ],
    }


def markdown(report: dict) -> str:
    summary = report["summary"]
    lines = [
        "# WeChat article source risk inventory",
        "",
        f"- HTML files: {summary['html_files']}",
        f"- Assets: {summary['assets']}",
        f"- References: {summary['references']}",
        f"- Remote dependencies: {summary['remote_dependencies']}",
        f"- External destinations: {summary['external_destinations']}",
        f"- Missing local assets: {summary['missing_local_assets']}",
        "",
        "## Findings",
        "",
    ]
    if not report["findings"]:
        lines.append("No static source risks detected by this scanner.")
    else:
        lines.extend(["| Severity | Rule | File:line | Finding | Evidence |", "| --- | --- | --- | --- | --- |"])
        for item in report["findings"]:
            location = item["file"] + (f":{item['line']}" if item["line"] else "")
            evidence = item["evidence"].replace("|", "\\|").replace("\n", " ")
            lines.append(f"| {item['severity']} | {item['rule_id']} | {location} | {item['message']} | `{evidence}` |")
    lines.extend(["", "## Asset manifest", "", "| Path | Type | Bytes | Dimensions | Frames | Duration ms |", "| --- | --- | ---: | --- | ---: | ---: |"])
    for asset in report["assets"]:
        dimensions = f"{asset.get('width', '')}x{asset.get('height', '')}" if "width" in asset else ""
        lines.append(f"| {asset['path']} | {asset['type']} | {asset['bytes']} | {dimensions} | {asset.get('frames', '')} | {asset.get('duration_ms', '')} |")
    lines.extend(["", "## Limitations", ""])
    lines.extend(f"- {item}" for item in report["limitations"])
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="HTML file, directory, or ZIP package")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = args.input.expanduser().resolve()
    if not source.exists():
        print(f"Input does not exist: {source}", file=sys.stderr)
        return 2
    rejected: list[str] = []
    with tempfile.TemporaryDirectory(prefix="wechat-source-audit-") as tmp:
        if source.is_file() and source.suffix.lower() == ".zip":
            root = Path(tmp)
            rejected = safe_extract(source, root)
        elif source.is_file() and source.suffix.lower() in {".html", ".htm"}:
            root = source.parent
            only_html = source
        elif source.is_dir():
            root = source
            only_html = None
        else:
            print("Input must be an HTML file, directory, or ZIP package.", file=sys.stderr)
            return 2
        if source.suffix.lower() == ".zip":
            only_html = None
        report = inspect_root(root, rejected, only_html)
        if args.format == "json":
            print(json.dumps(report, ensure_ascii=False, indent=2))
        else:
            print(markdown(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
