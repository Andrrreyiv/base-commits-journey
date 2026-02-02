#!/usr/bin/env python3
"""
Проверка относительных ссылок в Markdown: существование целевых файлов.
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


def extract_links(md_path):
    text = md_path.read_text(encoding="utf-8", errors="replace")
    # [text](url) и ](url)
    for m in re.finditer(r'\]\(([^)]+)\)', text):
        url = m.group(1).strip()
        if url.startswith("#") or "://" in url:
            continue
        yield url


def resolve_target(md_path, url):
    url = url.split("#")[0].strip()
    if not url:
        return None
    try:
        target = (md_path.parent / url).resolve()
        target.relative_to(ROOT)
        return target
    except (ValueError, OSError):
        return None


def main():
    errors = []
    for md_path in find_md_files():
        for url in extract_links(md_path):
            target = resolve_target(md_path, url)
            if target is None:
                continue
            if not target.exists():
                errors.append(f"{md_path.relative_to(ROOT)}: ссылка {url!r} ведёт к несуществующему пути")
    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        sys.exit(1)
    print("OK: все проверенные ссылки существуют.")
    sys.exit(0)


if __name__ == "__main__":
    main()
