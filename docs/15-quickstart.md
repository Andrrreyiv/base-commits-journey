# Quickstart: ежедневные коммиты

Краткий цикл для одного рабочего дня: что сделать, чтобы коммит был полезным и попал в историю.

## Цель

- За 5–10 минут понять, что делать сегодня.
- Сделать один или несколько атомарных коммитов без суеты.

## Шаги

1. **Открой репозиторий и подтяни изменения:**
   ```bash
   git switch main
   git pull
   ```

2. **Выбери одну задачу:** посмотри [PROGRESS.md](../PROGRESS.md) или [ROADMAP.md](../ROADMAP.md). Возьми следующую по списку или из раздела «Следующие 5 коммитов».

3. **Добавь строку в PROGRESS.md** (новый ID, Title, Acceptance criteria). Не коммить пока — это часть того же коммита.

4. **Сделай изменения:** создай/измени файлы по задаче (документация, скрипт, конфиг, тест).

5. **Проверь локально** (если есть скрипты):
   ```bash
   python scripts/check_links.py
   python scripts/validate_repo.py
   python scripts/check_markdown_hygiene.py
   ```
   Или: `make check` (если установлен make).

6. **Закоммить и отправить:**
   ```bash
   git add -A
   git status
   git diff --cached --stat
   git commit -m "Docs: краткое описание"
   git push
   ```

7. **Заполни в PROGRESS.md:** Files changed, Status = ✅ Done, Notes.

## Проверка

- На GitHub во вкладке **Commits** виден новый коммит с твоим сообщением.
- В PROGRESS.md появилась строка с Status ✅ Done.

## Типовые ошибки

- **Забыл обновить PROGRESS.md** — каждый коммит должен включать изменение PROGRESS.md.
- **Один коммит — несколько несвязанных правок** — разбей на два коммита или объедини задачу в одну мысль.
- **Push rejected** — выполни `git pull --rebase origin main`, затем снова `git push`.
