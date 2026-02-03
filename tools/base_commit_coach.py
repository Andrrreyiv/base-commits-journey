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


# Следующие задачи плана (94–100) для подсказки --next
PLAN_NEXT = [
    (94, "Tools: add next tasks suggestion from roadmap"),
    (95, "Docs: add daily workflow guide"),
    (96, "Docs: add weekly review guide"),
    (97, "Docs: add badges for license and last commit"),
    (98, "CI: add stale issues workflow"),
    (99, "Docs: document issue lifecycle"),
    (100, "Chore: phase 2 consistency pass"),
]


def cmd_next():
    """Подсказка: следующая задача из плана по номеру коммита."""
    try:
        r = subprocess.run(
            ["git", "rev-list", "--count", "HEAD"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        n = int(r.stdout.strip())
    except (subprocess.CalledProcessError, FileNotFoundError, ValueError):
        n = 0
    next_n = n + 1
    for num, title in PLAN_NEXT:
        if num == next_n:
            print(f"Следующий коммит: #{num} — {title}")
            print("Добавь строку в PROGRESS.md (следующий P-XXX), сделай изменения, git add, commit, push.")
            sys.exit(0)
    if next_n > 100:
        print("Цель 100 коммитов достигнута. Дальше: финальная вычитка, теги, релиз.")
    else:
        print(f"Следующий номер: {next_n}. Открой PROGRESS.md и ROADMAP.md для выбора задачи.")
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
