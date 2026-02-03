"""Tests for scripts/validate_progress_ids.py."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import scripts.validate_progress_ids as progress_ids


class TestValidateProgressIds(unittest.TestCase):
    def test_extract_ids_returns_list(self):
        ids = progress_ids.extract_ids()
        self.assertIsInstance(ids, list)
        self.assertGreater(len(ids), 0)

    def test_ids_follow_pattern(self):
        ids = progress_ids.extract_ids()
        for id_ in ids:
            self.assertTrue(id_.startswith("P-"), f"ID {id_!r} should start with P-")
