#!/usr/bin/env python3

from __future__ import annotations

import tempfile
import unittest
import zipfile
from pathlib import Path

import audit_source


class AuditSourceTests(unittest.TestCase):
    def test_distinguishes_destinations_from_asset_dependencies(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "index.html").write_text(
                '<a href="https://example.com/page">Page</a>'
                '<img src="https://example.com/image.png">',
                encoding="utf-8",
            )
            report = audit_source.inspect_root(root, [])
            rules = [item["rule_id"] for item in report["findings"]]
            self.assertIn("EXTERNAL_DESTINATION", rules)
            self.assertEqual(rules.count("REMOTE_DEPENDENCY"), 1)

    def test_detects_source_and_css_risks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "index.html").write_text(
                '<link rel="stylesheet" href="style.css">'
                '<img src="missing.png">'
                '<a href="javascript:void(0)" onclick="go()">Open</a>'
                '<iframe src="https://example.com/embed"></iframe>',
                encoding="utf-8",
            )
            (root / "style.css").write_text(
                '.panel { position: sticky; background: url("missing-bg.png"); }',
                encoding="utf-8",
            )
            report = audit_source.inspect_root(root, [])
            rules = {item["rule_id"] for item in report["findings"]}
            self.assertTrue({"TAG_IFRAME", "EVENT_HANDLER", "JAVASCRIPT_URL", "CSS_FIXED_STICKY"}.issubset(rules))
            self.assertEqual(report["summary"]["missing_local_assets"], 2)

    def test_clean_static_package_has_no_blockers(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "index.html").write_text('<img src="ok.svg" alt="complete static content">', encoding="utf-8")
            (root / "ok.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" width="10" height="10"/>', encoding="utf-8")
            report = audit_source.inspect_root(root, [])
            self.assertFalse(any(item["severity"] == "阻断" for item in report["findings"]))
            self.assertEqual(report["summary"]["missing_local_assets"], 0)

    def test_rejects_zip_path_traversal(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = root / "unsafe.zip"
            output = root / "output"
            output.mkdir()
            with zipfile.ZipFile(archive, "w") as zf:
                zf.writestr("../escape.html", "unsafe")
                zf.writestr("safe/index.html", "<p>safe</p>")
            rejected = audit_source.safe_extract(archive, output)
            self.assertEqual(rejected, ["../escape.html"])
            self.assertFalse((root / "escape.html").exists())


if __name__ == "__main__":
    unittest.main()
