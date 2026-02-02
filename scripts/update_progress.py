#!/usr/bin/env python3
"""
Обновляет строку «Progress: X/100» в README на основе git rev-list --count HEAD.
Только stdlib, без зависимостей. Требует git в PATH.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"


def get_commit_count():
    result = subprocess.run(
        ["git", "rev-list", "--count", "HEAD"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print("Ошибка: git rev-list --count HEAD не выполнился.", file=sys.stderr)
        sys.exit(1)
    return int(result.stdout.strip())


def main():
    count = get_commit_count()
    text = README.read_text(encoding="utf-8", errors="replace")
    pattern = r"(Progress:\s*)\d+(/100)"
    replacement = rf"\g<1>{count}\2"
    new_text, n = re.subn(pattern, replacement, text)
    if n == 0:
        # Строки может не быть — тогда не меняем
        print("Строка Progress: X/100 в README не найдена.", file=sys.stderr)
        sys.exit(0)
    README.write_text(new_text, encoding="utf-8")
    print(f"Обновлено: Progress: {count}/100 в README.")
    sys.exit(0)


if __name__ == "__main__":
    main()
