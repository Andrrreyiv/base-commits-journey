#!/usr/bin/env python3
"""
Проверка наличия ключевых файлов и папок в репозитории.
Только stdlib, без зависимостей.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED = [
    "README.md",
    "PROGRESS.md",
    "docs/README.md",
    ".gitignore",
]

OPTIONAL = [
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "scripts/",
]


def main():
    errors = []
    for name in REQUIRED:
        path = ROOT / name
        if not path.exists():
            errors.append(f"Отсутствует обязательный путь: {name}")
    for name in OPTIONAL:
        path = ROOT / name
        if not path.exists():
            print(f"Предупреждение: отсутствует {name}", file=sys.stderr)
    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        sys.exit(1)
    print("OK: все обязательные файлы/папки на месте.")
    sys.exit(0)


if __name__ == "__main__":
    main()
