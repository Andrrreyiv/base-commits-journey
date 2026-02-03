"""Tests for scripts/check_large_files.py."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

THRESHOLD = 1024 * 1024


class TestLargeFiles(unittest.TestCase):
    def test_threshold_defined(self):
        self.assertEqual(THRESHOLD, 1024 * 1024)

    def test_scripts_dir_has_check_large_files(self):
        p = ROOT / "scripts" / "check_large_files.py"
        self.assertTrue(p.exists())
        self.assertLess(p.stat().st_size, THRESHOLD)
