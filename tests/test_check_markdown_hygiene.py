"""Tests for scripts/check_markdown_hygiene.py."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import scripts.check_markdown_hygiene as hygiene


class TestMarkdownHygiene(unittest.TestCase):
    def test_find_md_files_includes_docs(self):
        files = list(hygiene.find_md_files())
        paths = [str(p) for p in files]
        self.assertTrue(any("docs" in p for p in paths))

    def test_check_file_returns_list(self):
        errors = hygiene.check_file(ROOT / "README.md")
        self.assertIsInstance(errors, list)
