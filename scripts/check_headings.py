#!/usr/bin/env python3
"""
Проверка согласованности заголовков в Markdown: один # H1 на файл,
остальные уровни не пропускают (нет перехода с ## на ####).
Только stdlib.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def find_md_files():
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        yield path


def check_file(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    rel = path.relative_to(ROOT)
    errors = []
    lines = text.splitlines()
    for i, line in enumerate(lines, 1):
        if not line.startswith("#"):
            continue
        m = re.match(r"^(#{1,6})\s+(.+)$", line)
        if not m:
            continue
        level = len(m.group(1))
        if level == 1 and i > 1:
            errors.append(f"{rel}:{i}: H1 должен быть только в начале файла")
    prev_level = 0
    for i, line in enumerate(lines, 1):
        if not line.startswith("#"):
            continue
        m = re.match(r"^(#{1,6})\s+", line)
        if not m:
            continue
        level = len(m.group(1))
        if level > prev_level + 1 and prev_level > 0:
            errors.append(f"{rel}:{i}: пропуск уровня заголовка (был {prev_level}, стал {level})")
        prev_level = level
    return errors


def main():
    all_errors = []
    for path in find_md_files():
        all_errors.extend(check_file(path))
    if all_errors:
        for e in all_errors:
            print(e, file=sys.stderr)
        sys.exit(1)
    print("OK: заголовки Markdown согласованы.")
    sys.exit(0)


if __name__ == "__main__":
    main()
