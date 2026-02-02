# Использование скриптов

Как запускать скрипты из `scripts/`, примеры команд и типовые ошибки.

## Цель

- Запускать проверки локально перед коммитом и PR.
- Понимать, что делает каждый скрипт и как исправить типовые ошибки.

## Скрипты

Все скрипты — только Python stdlib, без зависимостей. Запуск из корня репозитория.

### check_links.py

Проверяет относительные ссылки в Markdown: целевой файл должен существовать.

```bash
python scripts/check_links.py
```

**Типовые ошибки:** «ссылка ведёт к несуществующему пути» — исправь путь в документе или создай файл.

### validate_repo.py

Проверяет наличие обязательных файлов/папок (README.md, PROGRESS.md, docs/README.md, .gitignore).

```bash
python scripts/validate_repo.py
```

**Типовые ошибки:** «Отсутствует обязательный путь» — добавь недостающий файл или обнови список в скрипте.

### check_markdown_hygiene.py

Проверяет: финальный перевод строки, LF (не CRLF), отсутствие trailing spaces, отсутствие тройных пустых строк.

```bash
python scripts/check_markdown_hygiene.py
```

**Типовые ошибки:** «trailing spaces» — удали пробелы в конце строки; «отсутствует финальный перевод строки» — добавь пустую строку в конец файла.

### update_progress.py

Обновляет в README строку вида «Progress: X/100» по числу коммитов (`git rev-list --count HEAD`). Требует git в PATH.

```bash
python scripts/update_progress.py
```

**Типовые ошибки:** «git rev-list не выполнился» — убедись, что находишься в корне репо и git установлен.

## Рекомендации

- Перед коммитом: `python scripts/check_links.py && python scripts/validate_repo.py && python scripts/check_markdown_hygiene.py`.
- В CI эти скрипты запускаются автоматически при push и PR.
