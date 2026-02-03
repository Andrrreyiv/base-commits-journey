"""Tests for scripts/check_links.py."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import scripts.check_links as check_links


class TestCheckLinks(unittest.TestCase):
    def test_extract_links_finds_links(self):
        ids = list(check_links.extract_links(ROOT / "PROGRESS.md"))
        self.assertIsInstance(ids, list)

    def test_resolve_target_skips_anchor(self):
        md = ROOT / "README.md"
        target = check_links.resolve_target(md, "docs/README.md#section")
        self.assertIsNotNone(target)
        self.assertEqual(target.name, "README.md")
