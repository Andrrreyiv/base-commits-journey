"""Tests for scripts/check_headings.py."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import scripts.check_headings as headings


class TestCheckHeadings(unittest.TestCase):
    def test_find_md_files(self):
        files = list(headings.find_md_files())
        self.assertGreater(len(files), 0)

    def test_check_file_returns_list(self):
        p = ROOT / "README.md"
        errors = headings.check_file(p)
        self.assertIsInstance(errors, list)
