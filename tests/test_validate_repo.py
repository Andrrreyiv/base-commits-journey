"""Tests for scripts/validate_repo.py."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class TestValidateRepo(unittest.TestCase):
    def test_required_files_exist(self):
        self.assertTrue((ROOT / "README.md").exists())
        self.assertTrue((ROOT / "PROGRESS.md").exists())
        self.assertTrue((ROOT / "docs" / "README.md").exists())
        self.assertTrue((ROOT / ".gitignore").exists())

    def test_scripts_dir_exists(self):
        self.assertTrue((ROOT / "scripts").is_dir())
