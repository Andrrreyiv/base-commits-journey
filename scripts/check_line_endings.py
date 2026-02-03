#!/usr/bin/env python3
"""
Проверка переносов строк: в текстовых файлах должен быть LF, не CRLF.
Только stdlib.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXTENSIONS = {".md", ".py", ".yml", ".yaml", ".json"}
MAX_SIZE = 1024 * 1024


def main():
    errors = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.suffix not in EXTENSIONS:
            continue
        if path.stat().st_size > MAX_SIZE:
            continue
        try:
            raw = path.read_bytes()
        except OSError:
            continue
        if b"\r\n" in raw or raw.endswith(b"\r"):
            errors.append(f"{path.relative_to(ROOT)}: найдены CRLF или CR")
    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        sys.exit(1)
    print("OK: переносы строк (LF) в порядке.")
    sys.exit(0)


if __name__ == "__main__":
    main()
