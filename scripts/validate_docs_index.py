#!/usr/bin/env python3
"""
Проверка: нумерованные ссылки в docs/README.md (01-goal..NN-name.md) соответствуют
существующим файлам в docs/, и все такие .md файлы упомянуты в оглавлении.
Только stdlib.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
INDEX = DOCS / "README.md"


def get_indexed_files():
    """Из docs/README.md извлекаем ссылки вида (NN-name.md)."""
    if not INDEX.exists():
        return []
    text = INDEX.read_text(encoding="utf-8", errors="replace")
    files = set()
    for m in re.finditer(r"\]\((\d{2}-[^)]+\.md)\)", text):
        files.add(m.group(1))
    return files


def get_actual_guides():
    """Все .md в docs/, кроме README, FAQ, GLOSSARY, _template."""
    skip = {"README.md", "FAQ.md", "GLOSSARY.md", "_template.md"}
    return [
        f.name
        for f in DOCS.iterdir()
        if f.suffix == ".md" and f.name not in skip
    ]


def main():
    if not DOCS.exists():
        print("Ошибка: папка docs/ не найдена.", file=sys.stderr)
        sys.exit(1)
    indexed = get_indexed_files()
    actual = set(get_actual_guides())
    missing_in_index = actual - indexed
    missing_on_disk = indexed - actual
    if missing_on_disk:
        for f in sorted(missing_on_disk):
            print(f"Ошибка: в оглавлении указан {f}, но файл не найден в docs/.", file=sys.stderr)
        sys.exit(1)
    if missing_in_index:
        for f in sorted(missing_in_index):
            print(f"Ошибка: файл docs/{f} не упомянут в docs/README.md.", file=sys.stderr)
        sys.exit(1)
    print("OK: оглавление docs/README.md соответствует файлам в docs/.")
    sys.exit(0)


if __name__ == "__main__":
    main()
