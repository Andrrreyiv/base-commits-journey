#!/usr/bin/env python3
"""
Добавляет запись в секцию Unreleased в CHANGELOG.md.
Использование: python scripts/add_changelog_entry.py "Добавлено" "Описание пункта"
Только stdlib.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHANGELOG = ROOT / "CHANGELOG.md"

UNRELEASED = "## [Unreleased]"


def main():
    if len(sys.argv) < 3:
        print("Использование: python add_changelog_entry.py <Секция> <Текст>", file=sys.stderr)
        print("Пример: python add_changelog_entry.py Добавлено Гайд по отладке CI.", file=sys.stderr)
        sys.exit(1)
    section = sys.argv[1]
    text = sys.argv[2]
    if not CHANGELOG.exists():
        print("Ошибка: CHANGELOG.md не найден.", file=sys.stderr)
        sys.exit(1)
    content = CHANGELOG.read_text(encoding="utf-8", errors="replace")
    if UNRELEASED not in content:
        print("Ошибка: секция [Unreleased] не найдена в CHANGELOG.md.", file=sys.stderr)
        sys.exit(1)
    bullet = f"- {text}\n"
    idx = content.find(UNRELEASED)
    add_section = content.find("### Добавлено", idx)
    if add_section == -1:
        add_section = content.find("\n\n", idx) + 2 if content.find("\n\n", idx) != -1 else idx
    end_of_line = content.find("\n", add_section) + 1
    new_content = content[:end_of_line] + bullet + content[end_of_line:]
    CHANGELOG.write_text(new_content, encoding="utf-8")
    print(f"Добавлена запись в [Unreleased]: {section} — {text}")
    sys.exit(0)


if __name__ == "__main__":
    main()
