#!/usr/bin/env python3
"""Check a layered HTML/CSS template package for portable local delivery."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote


REQUIRED_FILES = ("index.html", "styles.css", "template-manifest.json")
REMOTE_RE = re.compile(r"^(?:https?:)?//", re.IGNORECASE)
CSS_URL_RE = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.IGNORECASE)


class ResourceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.resources: list[str] = []
        self.has_iframe = False
        self.has_layer = False
        self.has_field = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        self.has_iframe |= tag.lower() == "iframe"
        self.has_layer |= "data-layer" in values
        self.has_field |= "data-field" in values or "contenteditable" in values
        for name in ("src", "href", "poster"):
            value = values.get(name)
            if value:
                self.resources.append(value)


def normalize_reference(value: str) -> str | None:
    value = unquote(value.strip()).split("#", 1)[0].split("?", 1)[0]
    if not value or value.startswith("#"):
        return None
    return value


def check_resource(root: Path, owner: Path, value: str, errors: list[str]) -> None:
    normalized = normalize_reference(value)
    if normalized is None:
        return
    if REMOTE_RE.match(normalized) or normalized.startswith(("data:", "file:")):
        errors.append(f"non-relative resource in {owner.relative_to(root)}: {value}")
        return
    if Path(normalized).is_absolute():
        errors.append(f"absolute resource in {owner.relative_to(root)}: {value}")
        return
    target = (owner.parent / normalized).resolve()
    try:
        target.relative_to(root.resolve())
    except ValueError:
        errors.append(f"resource escapes package in {owner.relative_to(root)}: {value}")
        return
    if not target.is_file():
        errors.append(f"missing resource in {owner.relative_to(root)}: {value}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("package", type=Path)
    args = parser.parse_args()
    root = args.package.resolve()
    errors: list[str] = []
    warnings: list[str] = []

    if not root.is_dir():
        print(f"FAIL package directory not found: {root}")
        return 1

    for name in REQUIRED_FILES:
        if not (root / name).is_file():
            errors.append(f"missing required file: {name}")

    html_files = sorted(root.rglob("*.html"))
    css_files = sorted(root.rglob("*.css"))
    if not html_files:
        errors.append("no HTML files found")
    if not css_files:
        errors.append("no CSS files found")

    has_layer = False
    has_field = False
    for path in html_files:
        source = path.read_text(encoding="utf-8")
        html = ResourceParser()
        html.feed(source)
        has_layer |= html.has_layer
        has_field |= html.has_field
        if html.has_iframe:
            errors.append(f"iframe found in {path.relative_to(root)}")
        for value in html.resources:
            check_resource(root, path, value, errors)
        if re.search(r"web-sandbox\.oaiusercontent\.com", source, re.IGNORECASE):
            errors.append(f"web-sandbox URL found in {path.relative_to(root)}")

    for path in css_files:
        source = path.read_text(encoding="utf-8")
        if re.search(r"web-sandbox\.oaiusercontent\.com", source, re.IGNORECASE):
            errors.append(f"web-sandbox URL found in {path.relative_to(root)}")
        for _, value in CSS_URL_RE.findall(source):
            check_resource(root, path, value, errors)

    if not has_layer:
        errors.append("no data-layer attribute found")
    if not has_field:
        warnings.append("no data-field or contenteditable attribute found")

    manifest_path = root / "template-manifest.json"
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            canvas = manifest.get("canvas", {})
            if not isinstance(canvas.get("width"), (int, float)) or canvas["width"] <= 0:
                errors.append("manifest canvas.width must be positive")
            if not isinstance(canvas.get("height"), (int, float)) or canvas["height"] <= 0:
                errors.append("manifest canvas.height must be positive")
            source_reference = manifest.get("sourceReference")
            if not source_reference:
                errors.append("manifest sourceReference is missing")
            else:
                check_resource(root, manifest_path, str(source_reference), errors)
            if not manifest.get("layers"):
                errors.append("manifest layers are missing")
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            errors.append(f"invalid template-manifest.json: {exc}")

    for warning in warnings:
        print(f"WARN {warning}")
    if errors:
        for error in dict.fromkeys(errors):
            print(f"FAIL {error}")
        return 1

    print(f"PASS {root}")
    print(f"HTML {len(html_files)} | CSS {len(css_files)} | local resources resolved")
    return 0


if __name__ == "__main__":
    sys.exit(main())
