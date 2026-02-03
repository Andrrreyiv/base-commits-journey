"""Tests for scripts/validate_docs_index.py."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import scripts.validate_docs_index as docs_index


class TestValidateDocsIndex(unittest.TestCase):
    def test_get_indexed_files_returns_set(self):
        files = docs_index.get_indexed_files()
        self.assertIsInstance(files, set)

    def test_docs_readme_exists(self):
        self.assertTrue(docs_index.INDEX.exists())
