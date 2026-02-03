#!/usr/bin/env python3
"""
Base Commit Coach CLI: подсказки по следующему шагу и отчёт по прогрессу.
Только stdlib.
"""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def cmd_report():
    """Вывести краткий отчёт: число коммитов, последние записи PROGRESS."""
    try:
        n = subprocess.run(
            ["git", "rev-list", "--count", "HEAD"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        print(f"Коммитов на main: {n.stdout.strip()}")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Не удалось получить число коммитов (git?).")
    if (ROOT / "PROGRESS.md").exists():
        text = (ROOT / "PROGRESS.md").read_text(encoding="utf-8", errors="replace")
        count = text.count("| P-")
        print(f"Записей в PROGRESS: {count}")
    sys.exit(0)


def cmd_next():
    """Подсказка: следующая задача из ROADMAP/PROGRESS."""
    print("Следующий шаг: открой PROGRESS.md или ROADMAP.md, выбери следующую задачу по ID.")
    print("Затем: добавь строку в PROGRESS, сделай изменения, git add, commit, push.")
    sys.exit(0)


def main():
    parser = argparse.ArgumentParser(description="Base Commit Coach — подсказки по коммитам.")
    parser.add_argument("--report", action="store_true", help="Краткий отчёт по прогрессу")
    parser.add_argument("--next", action="store_true", dest="next_", help="Подсказка: следующая задача")
    args = parser.parse_args()
    if args.report:
        cmd_report()
    if args.next_:
        cmd_next()
    if not (args.report or args.next_):
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
