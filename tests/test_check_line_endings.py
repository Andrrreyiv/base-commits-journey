"""Tests for scripts/check_line_endings.py."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class TestLineEndings(unittest.TestCase):
    def test_scripts_exist(self):
        self.assertTrue((ROOT / "scripts" / "check_line_endings.py").exists())

    def test_root_has_md_files(self):
        readme = ROOT / "README.md"
        self.assertTrue(readme.exists())
