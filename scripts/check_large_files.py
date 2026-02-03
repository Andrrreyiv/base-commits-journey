#!/usr/bin/env python3
"""
Проверка размера файлов: предупреждение или ошибка, если файл превышает порог.
Только stdlib. По умолчанию порог 1 MiB.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
THRESHOLD_MIB = 1
THRESHOLD = THRESHOLD_MIB * 1024 * 1024


def main():
    large = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        try:
            size = path.stat().st_size
        except OSError:
            continue
        if size > THRESHOLD:
            large.append((path.relative_to(ROOT), size))
    if large:
        for rel, size in sorted(large, key=lambda x: -x[1]):
            mib = size / (1024 * 1024)
            print(f"{rel}: {mib:.1f} MiB", file=sys.stderr)
        sys.exit(1)
    print("OK: нет файлов больше 1 MiB.")
    sys.exit(0)


if __name__ == "__main__":
    main()
