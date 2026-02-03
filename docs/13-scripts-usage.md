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

### validate_progress_ids.py

Проверяет, что в PROGRESS.md ID в таблице идут подряд без пропусков и дубликатов (P-001, P-002, …).

```bash
python scripts/validate_progress_ids.py
```

**Типовые ошибки:** «ожидался P-00X, найден P-00Y» — добавь недостающую строку или исправь порядок в таблице; «дубликат ID» — удали или переименуй дубликат.

### validate_docs_index.py

Проверяет, что нумерованные гайды в docs/ (01-name.md … NN-name.md) перечислены в docs/README.md и все указанные в оглавлении файлы существуют.

```bash
python scripts/validate_docs_index.py
```

**Типовые ошибки:** «файл не найден в docs/» — создай файл или убери ссылку из оглавления; «файл не упомянут в docs/README.md» — добавь пункт в оглавление.

### check_headings.py

Проверяет согласованность заголовков в Markdown: один H1 на файл, без пропуска уровней (например не ## сразу ####).

```bash
python scripts/check_headings.py
```

**Типовые ошибки:** «H1 должен быть только в начале» — оставь один # в начале; «пропуск уровня заголовка» — добавь промежуточный уровень (## перед ####).

### add_changelog_entry.py

Добавляет пункт в секцию [Unreleased] в CHANGELOG.md. Аргументы: секция (например «Добавлено»), текст.

```bash
python scripts/add_changelog_entry.py "Добавлено" "Краткое описание"
```

**Типовые ошибки:** «секция [Unreleased] не найдена» — добавь блок ## [Unreleased] в CHANGELOG.

### check_line_endings.py

Проверяет, что в .md, .py, .yml, .json нет CRLF (только LF).

```bash
python scripts/check_line_endings.py
```

**Типовые ошибки:** «найдены CRLF» — сохрани файл с LF (EditorConfig или настройки редактора).

### check_large_files.py

Проверяет, что нет файлов больше 1 MiB (чтобы не заносить в репо случайно большие бинарники).

```bash
python scripts/check_large_files.py
```

**Типовые ошибки:** добавь файл в .gitignore или увеличь порог в скрипте при необходимости.

### roadmap_stats.py

Выводит краткую статистику: число записей в PROGRESS, число этапов в ROADMAP. Для CI summary и локальной проверки.

```bash
python scripts/roadmap_stats.py
```

## Рекомендации

- Перед коммитом: `python scripts/check_links.py && python scripts/validate_repo.py && python scripts/check_markdown_hygiene.py && python scripts/validate_progress_ids.py`.
- В CI эти скрипты запускаются автоматически при push и PR.
