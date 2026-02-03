#!/usr/bin/env python3
"""
Выводит краткую статистику по ROADMAP и PROGRESS: число задач/этапов.
Только stdlib. Для использования в CI и локально.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROGRESS = ROOT / "PROGRESS.md"
ROADMAP = ROOT / "ROADMAP.md"


def main():
    lines = []
    if PROGRESS.exists():
        text = PROGRESS.read_text(encoding="utf-8", errors="replace")
        count = text.count("| P-")
        lines.append(f"PROGRESS: {count} записей (P-001..P-{count:03d})")
    if ROADMAP.exists():
        text = ROADMAP.read_text(encoding="utf-8", errors="replace")
        stages = text.count("## Этап")
        if not stages:
            stages = text.count("## ")
        lines.append(f"ROADMAP: этапов/секций ~{stages}")
    for line in lines:
        print(line)
    sys.exit(0)


if __name__ == "__main__":
    main()
