#!/usr/bin/env python3
"""Check design evidence completeness, not aesthetic quality or truthfulness."""

import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

CRITERIA = {"content", "drawing_style", "graphic_extension", "composition", "reading", "technical"}
VISUAL = {"drawing_style", "graphic_extension", "composition", "reading"}
STATUSES = {"pass", "fail", "not_checked", "not_applicable"}
VIEW_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif", ".bmp", ".tif", ".tiff", ".svg", ".pdf"}


class Validator:
    def __init__(self, base):
        self.base = base
        self.errors = []
        self.blocked = []

    def error(self, message):
        self.errors.append(message)

    def string(self, value, label, required=True):
        if not isinstance(value, str) or (required and not value.strip()):
            self.error(f"{label}: requires {'nonempty ' if required else ''}text")
            return ""
        return value.strip()

    def object(self, value, label):
        if not isinstance(value, dict):
            self.error(f"{label}: requires object")
            return {}
        return value

    def array(self, value, label):
        if not isinstance(value, list):
            self.error(f"{label}: requires array")
            return []
        return value

    def file(self, value, label, required=True, visual=False):
        if value in (None, "") and not required:
            return None
        value = self.string(value, label)
        if not value:
            return None
        try:
            path = (self.base / value).resolve()
            if not path.is_file():
                self.error(f"{label}: file does not exist")
                return None
            if visual and path.suffix.lower() not in VIEW_EXTENSIONS:
                self.error(f"{label}: requires image or visual preview")
                return None
            return path
        except (OSError, ValueError):
            self.error(f"{label}: invalid path")
            return None

    def source(self, value, label):
        value = self.string(value, label)
        if not value:
            return None
        parsed = urlparse(value)
        if parsed.scheme in {"http", "https"} and parsed.netloc:
            return value
        return self.file(value, label)

    def paths(self, value, label, required=False, visual=False):
        values = self.array(value, label)
        if required and not values:
            self.error(f"{label}: requires at least one file")
        return [path for i, raw in enumerate(values)
                if (path := self.file(raw, f"{label}[{i}]", visual=visual)) is not None]

    def status(self, item, label, allow_na=True):
        status = item.get("status")
        if status not in STATUSES:
            self.error(f"{label}.status: invalid status")
            return None
        self.string(item.get("evidence"), f"{label}.evidence")
        if status == "not_applicable" and not allow_na:
            self.error(f"{label}: not_applicable contradicts task scope")
        if status in {"fail", "not_checked"}:
            self.blocked.append(f"{label}: {status}")
        return status

    def ids(self, value, label, rules, required=False):
        values = self.array(value, label)
        if required and not values:
            self.error(f"{label}: requires corresponding rules")
        ids = set()
        for i, raw in enumerate(values):
            ident = self.string(raw, f"{label}[{i}]")
            if ident not in rules:
                self.error(f"{label}: unknown rule {ident!r}")
            ids.add(ident)
        return ids

    def validate(self, raw):
        record = self.object(raw, "record")
        task = record.get("task_type")
        if task not in {"production", "review", "plan"}:
            self.error("task_type: expected production, review or plan")
        for field in ("has_style_reference", "has_drawing_task", "needs_graphic_extension"):
            if type(record.get(field)) is not bool:
                self.error(f"{field}: requires boolean task scope")
        style = record.get("has_style_reference") is True
        drawing = record.get("has_drawing_task") is True
        extension = record.get("needs_graphic_extension") is True

        rules = {}
        for i, value in enumerate(self.array(record.get("reference_rules"), "reference_rules")):
            label = f"reference_rules[{i}]"
            rule = self.object(value, label)
            ident = self.string(rule.get("id"), f"{label}.id")
            source = self.source(rule.get("source"), f"{label}.source")
            self.string(rule.get("observation"), f"{label}.observation")
            self.string(rule.get("requirement"), f"{label}.requirement")
            if type(rule.get("critical")) is not bool:
                self.error(f"{label}.critical: requires boolean")
            if ident in rules:
                self.error(f"{label}.id: duplicate rule")
            rules[ident] = {"source": source, "critical": rule.get("critical") is True}
        critical = {key for key, value in rules.items() if value["critical"]}
        if (style or drawing or extension) and not critical:
            self.error("reference_rules: task needs at least one critical visual rule")

        if task in {"production", "plan"}:
            composition = self.object(record.get("composition"), "composition")
            self.file(composition.get("overview_path"), "composition.overview_path",
                      visual=True)
            self.status(composition, "composition", allow_na=False)

        if task == "production":
            for i, value in enumerate(self.array(record.get("assets"), "assets")):
                label = f"assets[{i}]"
                asset = self.object(value, label)
                path = self.file(asset.get("path"), f"{label}.path")
                generated = asset.get("generated")
                if type(generated) is not bool:
                    self.error(f"{label}.generated: requires boolean")
                if generated is True and not drawing:
                    self.error("has_drawing_task: generated imagery requires visual drawing checks")
                self.status(asset, label, allow_na=generated is False)
                self.file(asset.get("prompt_path"), f"{label}.prompt_path", required=generated is True)
                ids = self.ids(asset.get("rule_ids", []), f"{label}.rule_ids", rules,
                               required=generated is True)
                sources = [self.source(raw, f"{label}.reference_sources[{j}]")
                           for j, raw in enumerate(self.array(asset.get("reference_sources", []),
                                                              f"{label}.reference_sources"))]
                comparison = self.paths(asset.get("comparison_paths", []),
                                        f"{label}.comparison_paths", visual=True)
                if generated is True:
                    if style and not sources:
                        self.error(f"{label}.reference_sources: generated asset needs actual reference")
                    if style and any(rules[key]["source"] not in sources for key in ids if key in rules):
                        self.error(f"{label}: references do not cover the cited rules")
                    if len(set(comparison)) < (2 if style else 1) or path not in comparison:
                        self.error(f"{label}.comparison_paths: include asset and reference/comparison view")

        if task in {"production", "review"}:
            outputs = self.array(record.get("outputs"), "outputs")
            if not outputs:
                self.error("outputs: requires final files")
            output_ids = set()
            for i, value in enumerate(outputs):
                label = f"outputs[{i}]"
                output = self.object(value, label)
                ident = self.string(output.get("id"), f"{label}.id")
                if ident in output_ids:
                    self.error(f"{label}.id: duplicate output")
                output_ids.add(ident)
                if output.get("type") not in {"poster", "longform", "other"}:
                    self.error(f"{label}.type: invalid output type")
                self.file(output.get("path"), f"{label}.path")

            seen, covered = set(), set()
            for i, value in enumerate(self.array(record.get("checks"), "checks")):
                label = f"checks[{i}]"
                check = self.object(value, label)
                criterion = check.get("criterion")
                if criterion not in CRITERIA:
                    self.error(f"{label}.criterion: invalid criterion")
                if criterion in seen:
                    self.error(f"{label}.criterion: duplicate check")
                seen.add(criterion)
                allow_na = ((criterion == "drawing_style" and not (style or drawing))
                            or (criterion == "graphic_extension" and not extension))
                status = self.status(check, label, allow_na=allow_na)
                self.paths(check.get("view_paths", []), f"{label}.view_paths",
                           required=status == "pass", visual=criterion in VISUAL)
                ids = self.ids(check.get("rule_ids", []), f"{label}.rule_ids", rules)
                if criterion in {"drawing_style", "graphic_extension"} and status != "not_applicable":
                    covered.update(ids)
            missing = CRITERIA - seen
            if missing:
                self.error("checks: missing " + ", ".join(sorted(missing)))
            if critical - covered:
                self.error("checks: critical rules not covered by drawing_style/graphic_extension: "
                           + ", ".join(sorted(critical - covered)))
        return task


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path, help="project design-evidence.json")
    args = parser.parse_args()
    try:
        raw = json.loads(args.record.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as exc:
        print(json.dumps({"status": "invalid_record", "error": str(exc)}, ensure_ascii=False))
        return 2
    validator = Validator(args.record.resolve().parent)
    try:
        task = validator.validate(raw)
    except (TypeError, ValueError, OSError) as exc:
        validator.error(f"invalid field: {exc}")
        task = None
    if validator.errors:
        result = {"status": "invalid_record", "errors": validator.errors[:5]}
        if len(validator.errors) > 5:
            result["additional_errors"] = len(validator.errors) - 5
        code = 2
    elif validator.blocked:
        result = {"status": "blocked", "items": validator.blocked[:5]}
        code = 3
    else:
        result = {"status": "record_complete", "task_type": task,
                  "meaning": "仅方案记录完整" if task == "plan" else "证据记录齐全；不代表审美合格"}
        code = 0
    print(json.dumps(result, ensure_ascii=False))
    return code


if __name__ == "__main__":
    sys.exit(main())
