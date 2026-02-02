#!/usr/bin/env python3
"""
Проверка гигиены Markdown: trailing spaces, двойные пустые строки, финальный перевод строки.
Только stdlib, без зависимостей.
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
    errors = []
    text = path.read_text(encoding="utf-8", errors="replace")
    rel = path.relative_to(ROOT)
    if text and not text.endswith("\n"):
        errors.append(f"{rel}: отсутствует финальный перевод строки")
    if "\r" in text:
        errors.append(f"{rel}: найдены CRLF, ожидается LF")
    for i, line in enumerate(text.splitlines(), 1):
        if line.rstrip() != line and line.strip():
            errors.append(f"{rel}:{i}: trailing spaces")
    if re.search(r"\n\n\n+", text):
        errors.append(f"{rel}: двойные или лишние пустые строки")
    return errors


def main():
    all_errors = []
    for path in find_md_files():
        all_errors.extend(check_file(path))
    if all_errors:
        for e in all_errors:
            print(e, file=sys.stderr)
        sys.exit(1)
    print("OK: гигиена Markdown в порядке.")
    sys.exit(0)


if __name__ == "__main__":
    main()
