#!/usr/bin/env python3
"""
Проверка последовательности ID в PROGRESS.md: P-001, P-002, ... без пропусков и дубликатов.
Только stdlib.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROGRESS = ROOT / "PROGRESS.md"


def extract_ids():
    text = PROGRESS.read_text(encoding="utf-8", errors="replace")
    ids = []
    for m in re.finditer(r"\|\s*(P-\d+)\s*\|", text):
        ids.append(m.group(1))
    return ids


def main():
    if not PROGRESS.exists():
        print("Ошибка: PROGRESS.md не найден.", file=sys.stderr)
        sys.exit(1)
    ids = extract_ids()
    if not ids:
        print("Предупреждение: в PROGRESS.md не найдено ни одного ID вида P-XXX.", file=sys.stderr)
        sys.exit(0)
    seen = set()
    for id_ in ids:
        if id_ in seen:
            print(f"Ошибка: дубликат ID {id_}.", file=sys.stderr)
            sys.exit(1)
        seen.add(id_)
    nums = sorted(int(id_.split("-")[1]) for id_ in ids)
    n = len(nums)
    for i in range(1, n + 1):
        if nums[i - 1] != i:
            print(f"Ошибка: ожидался P-{i:03d}, пропуск или неверный порядок (найдены номера {nums}).", file=sys.stderr)
            sys.exit(1)
    print(f"OK: последовательность ID в порядке (P-001..P-{n:03d}).")
    sys.exit(0)


if __name__ == "__main__":
    main()
