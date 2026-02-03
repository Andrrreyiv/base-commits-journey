# Mini-Issue Tracker (Progress)

Каждый коммит = одна закрытая mini-issue. Перед коммитом добавляется строка в таблицу, после выполнения — заполняются Files changed, Status = ✅ Done.

## Формат записи

| ID | Date | Title | Acceptance criteria | Files changed | Status | Notes |
|----|------|-------|---------------------|---------------|--------|-------|
| P-084 | 2025-02-02 | Tests: add tests for docs index validator | 1) tests/test_validate_docs_index.py. 2) Тесты для validate_docs_index. | tests/test_validate_docs_index.py, PROGRESS.md | ✅ Done | Тесты оглавления docs. |
| P-083 | 2025-02-02 | Tests: add tests for progress id validator | 1) tests/test_validate_progress_ids.py. 2) Тесты для validate_progress_ids. | tests/test_validate_progress_ids.py, PROGRESS.md | ✅ Done | Тесты валидации ID. |
| P-082 | 2025-02-02 | Tests: add tests for markdown hygiene checker | 1) tests/test_check_markdown_hygiene.py. 2) Тесты для check_markdown_hygiene. | tests/test_check_markdown_hygiene.py, PROGRESS.md | ✅ Done | Тесты гигиены Markdown. |
| P-081 | 2025-02-02 | Tests: add tests for repo validator | 1) tests/test_validate_repo.py. 2) Тесты для validate_repo. | tests/test_validate_repo.py, PROGRESS.md | ✅ Done | Тесты валидации репо. |
| P-080 | 2025-02-02 | Tests: add tests for link checker | 1) tests/test_check_links.py. 2) Тесты для check_links. | tests/test_check_links.py, PROGRESS.md | ✅ Done | Тесты проверки ссылок. |
| P-079 | 2025-02-02 | CI: run unit tests in workflow | 1) ci.yml: python -m unittest discover -v. | .github/workflows/ci.yml, PROGRESS.md | ✅ Done | CI запускает тесты. |
| P-078 | 2025-02-02 | Tests: add unittest scaffolding | 1) tests/README.md, tests/__init__.py. 2) Структура для unittest. | tests/README.md, tests/__init__.py, PROGRESS.md | ✅ Done | Каркас тестов. |
| P-077 | 2025-02-02 | CI: wire large files checker into workflow | 1) ci.yml: запуск check_large_files.py. | .github/workflows/ci.yml, PROGRESS.md | ✅ Done | CI проверяет размер файлов. |
| P-076 | 2025-02-02 | Scripts: add large files checker | 1) scripts/check_large_files.py. 2) docs/13 обновлён. 3) Порог 1 MiB. | scripts/check_large_files.py, docs/13-scripts-usage.md, PROGRESS.md | ✅ Done | Проверка больших файлов. |
| P-075 | 2025-02-02 | CI: wire line endings checker into workflow | 1) ci.yml: запуск check_line_endings.py. | .github/workflows/ci.yml, PROGRESS.md | ✅ Done | CI проверяет line endings. |
| P-074 | 2025-02-02 | Scripts: add line endings checker | 1) scripts/check_line_endings.py. 2) docs/13 обновлён. 3) LF, не CRLF. | scripts/check_line_endings.py, docs/13-scripts-usage.md, PROGRESS.md | ✅ Done | Проверка переносов строк. |
| P-073 | 2025-02-02 | Docs: add git hooks notes | 1) docs/27-git-hooks.md. 2) Заметки про pre-commit и др. | docs/27-git-hooks.md, PROGRESS.md | ✅ Done | Git hooks. |
| P-072 | 2025-02-02 | Docs: add labels setup instructions | 1) docs/26-labels-setup.md. 2) Создание меток на GitHub. | docs/26-labels-setup.md, PROGRESS.md | ✅ Done | Настройка labels. |
| P-071 | 2025-02-02 | Docs: add recommended labels reference | 1) docs/25-labels-reference.md. 2) Справочник меток. | docs/25-labels-reference.md, PROGRESS.md | ✅ Done | Справочник labels. |
| P-070 | 2025-02-02 | Docs: add verified email and contributions guide | 1) docs/24-verify-public-commits.md. 2) Ссылка в docs/README. 3) Verified email, как считаются contributions. | docs/24-verify-public-commits.md, docs/README.md, PROGRESS.md | ✅ Done | Верификация и contributions. |
| P-069 | 2025-02-02 | CI: add roadmap stats to workflow summary | 1) ci.yml: запуск roadmap_stats.py, вывод в summary. | .github/workflows/ci.yml, PROGRESS.md | ✅ Done | CI summary со статистикой. |
| P-068 | 2025-02-02 | Scripts: add roadmap stats script | 1) scripts/roadmap_stats.py создан. 2) docs/13-scripts-usage.md обновлён. 3) Статистика PROGRESS/ROADMAP. | scripts/roadmap_stats.py, docs/13-scripts-usage.md, PROGRESS.md | ✅ Done | Статистика по roadmap. |
| P-067 | 2025-02-02 | Docs: document changelog workflow | 1) docs/23-changelog-workflow.md создан. 2) Ссылка в docs/README.md. 3) Как вести CHANGELOG, хелпер. | docs/23-changelog-workflow.md, docs/README.md, PROGRESS.md | ✅ Done | Workflow CHANGELOG. |
| P-066 | 2025-02-02 | Scripts: add changelog entry helper | 1) scripts/add_changelog_entry.py создан. 2) docs/13-scripts-usage.md обновлён. 3) Добавление записи в CHANGELOG Unreleased. | scripts/add_changelog_entry.py, docs/13-scripts-usage.md, PROGRESS.md | ✅ Done | Хелпер для CHANGELOG. |
| P-065 | 2025-02-02 | CI: wire heading checker into workflow | 1) ci.yml: запуск check_headings.py. | .github/workflows/ci.yml, PROGRESS.md | ✅ Done | CI проверяет заголовки. |
| P-064 | 2025-02-02 | Scripts: add heading consistency checker | 1) scripts/check_headings.py создан. 2) docs/13-scripts-usage.md обновлён. 3) Один H1, без пропуска уровней. | scripts/check_headings.py, docs/13-scripts-usage.md, PROGRESS.md | ✅ Done | Согласованность заголовков. |
| P-063 | 2025-02-02 | Docs: add repository health checklist | 1) docs/22-repo-health-checklist.md создан. 2) Ссылка в docs/README.md. 3) Чеклист перед verify/релизом. | docs/22-repo-health-checklist.md, docs/README.md, PROGRESS.md | ✅ Done | Чеклист здоровья репо. |
| P-062 | 2025-02-02 | CI: add job summary output | 1) ci.yml: вывод в \$GITHUB_STEP_SUMMARY. 2) Краткий отчёт по проверкам. | .github/workflows/ci.yml, PROGRESS.md | ✅ Done | Итог CI в интерфейсе Actions. |
| P-061 | 2025-02-02 | Docs: add CI debugging guide | 1) docs/21-ci-debugging.md создан. 2) Ссылка в docs/README.md. 3) Как смотреть логи, типовые ошибки. | docs/21-ci-debugging.md, docs/README.md, PROGRESS.md | ✅ Done | Отладка CI. |
| P-060 | 2025-02-02 | CI: wire docs index validator into workflow | 1) ci.yml: запуск validate_docs_index.py. | .github/workflows/ci.yml, PROGRESS.md | ✅ Done | CI проверяет оглавление docs. |
| P-059 | 2025-02-02 | Scripts: add docs index validator | 1) scripts/validate_docs_index.py создан. 2) docs/13-scripts-usage.md обновлён. 3) Проверка соответствия docs/README.md и файлов в docs/. | scripts/validate_docs_index.py, docs/13-scripts-usage.md, PROGRESS.md | ✅ Done | Валидация оглавления docs. |
| P-058 | 2025-02-02 | CI: wire progress id validator into workflow | 1) ci.yml: запуск validate_progress_ids.py. | .github/workflows/ci.yml, PROGRESS.md | ✅ Done | CI проверяет ID в PROGRESS. |
| P-057 | 2025-02-02 | Scripts: add progress id validator | 1) scripts/validate_progress_ids.py создан. 2) docs/13-scripts-usage.md обновлён. 3) Проверка последовательности P-001..P-N в PROGRESS.md. | scripts/validate_progress_ids.py, docs/13-scripts-usage.md, PROGRESS.md | ✅ Done | Валидация ID в PROGRESS. |
| P-056 | 2025-02-02 | Docs: add templates usage guide | 1) docs/20-templates-howto.md создан. 2) Ссылка в docs/README.md. 3) Как пользоваться шаблонами issue и PR. | docs/20-templates-howto.md, docs/README.md, PROGRESS.md | ✅ Done | Гайд по шаблонам. |
| P-055 | 2025-02-02 | Docs: add issues and labels workflow guide | 1) docs/19-issues-labels-workflow.md создан. 2) Ссылка в docs/README.md. 3) Issues, метки, связь с PR. | docs/19-issues-labels-workflow.md, docs/README.md, PROGRESS.md | ✅ Done | Workflow issues и labels. |
| P-054 | 2025-02-02 | Docs: add tags and releases guide | 1) docs/18-tags-and-releases.md создан. 2) Ссылка в docs/README.md. 3) Создание тегов и Release. | docs/18-tags-and-releases.md, docs/README.md, PROGRESS.md | ✅ Done | Теги и релизы на GitHub. |
| P-053 | 2025-02-02 | Docs: add merge conflicts guide | 1) docs/17-merge-conflicts.md создан. 2) Ссылка в docs/README.md. 3) Как находить и разрешать конфликты. | docs/17-merge-conflicts.md, docs/README.md, PROGRESS.md | ✅ Done | Разрешение конфликтов слияния. |
| P-052 | 2025-02-02 | Docs: add undo reset revert guide | 1) docs/16-undo-reset-revert.md создан. 2) Ссылка в docs/README.md. 3) Различия undo/reset/revert, когда что применять. | docs/16-undo-reset-revert.md, docs/README.md, PROGRESS.md | ✅ Done | Безопасное откатывание изменений. |
| P-051 | 2025-02-02 | Docs: add quickstart guide for daily commits | 1) docs/15-quickstart.md создан. 2) Ссылка в docs/README.md. 3) Цель/шаги/проверка для ежедневных коммитов. | docs/15-quickstart.md, docs/README.md, PROGRESS.md | ✅ Done | Быстрый старт для ежедневной работы. |
| P-050 | 2025-02-02 | Chore: final consistency and formatting pass | 1) Единый стиль заголовков/ссылок/терминов. 2) Опечатки, рабочие ссылки. | несколько файлов, PROGRESS.md | ✅ Done | Финальная согласованность. |
| P-049 | 2025-02-02 | Chore: add dependabot config for GitHub Actions | 1) .github/dependabot.yml создан. 2) weekly для обновления actions. | .github/dependabot.yml, PROGRESS.md | ✅ Done | Автообновление actions. |
| P-048 | 2025-02-02 | Docs: add repository structure section | 1) README: дерево папок и назначение каждой. | README.md, PROGRESS.md | ✅ Done | Структура репо. |
| P-047 | 2025-02-02 | Docs: add CI badge and explanation | 1) README: бейдж CI, что проверяет, где смотреть логи. | README.md, PROGRESS.md | ✅ Done | Видимость статуса CI. |
| P-046 | 2025-02-02 | CI: add workflow_dispatch support | 1) ci.yml: workflow_dispatch для ручного запуска. | .github/workflows/ci.yml, PROGRESS.md | ✅ Done | Ручной запуск CI. |
| P-045 | 2025-02-02 | Docs: add Cursor workflow guide | 1) docs/14-cursor-workflow.md создан. 2) Как работать с агентом, diff, что не коммитить. | docs/14-cursor-workflow.md, PROGRESS.md | ✅ Done | Работа в Cursor. |
| P-044 | 2025-02-02 | Chore: add editor settings for Cursor/VS Code | 1) .vscode/settings.json + extensions.json созданы. 2) Аккуратно, без лишнего. | .vscode/settings.json, .vscode/extensions.json, PROGRESS.md | ✅ Done | Настройки редактора. |
| P-043 | 2025-02-02 | Chore: add Makefile with common commands | 1) Makefile создан. 2) targets check/links/validate/hygiene/progress + заметка для Windows. | Makefile, PROGRESS.md | ✅ Done | Удобные команды проверок. |
| P-042 | 2025-02-02 | Docs: document scripts usage | 1) docs/13-scripts-usage.md создан. 2) Как запускать scripts/*, примеры команд, типовые ошибки. | docs/13-scripts-usage.md, PROGRESS.md | ✅ Done | Документация по скриптам. |
| P-041 | 2025-02-02 | Scripts: add progress updater (stdlib) | 1) scripts/update_progress.py создан. 2) Обновляет строку Progress: X/100 в README по git rev-list --count HEAD. | scripts/update_progress.py, PROGRESS.md | ✅ Done | Автообновление счётчика. |
| P-040 | 2025-02-02 | CI: wire markdown hygiene into workflow | 1) ci.yml: запуск python scripts/check_markdown_hygiene.py. | .github/workflows/ci.yml, PROGRESS.md | ✅ Done | CI проверяет гигиену. |
| P-039 | 2025-02-02 | Scripts: add markdown hygiene checker (stdlib) | 1) scripts/check_markdown_hygiene.py создан. 2) trailing spaces, двойные пустые строки, финальный перевод строки. | scripts/check_markdown_hygiene.py, PROGRESS.md | ✅ Done | Гигиена Markdown. |
| P-038 | 2025-02-02 | CI: wire repo validator into workflow | 1) ci.yml: запуск python scripts/validate_repo.py. | .github/workflows/ci.yml, PROGRESS.md | ✅ Done | CI проверяет структуру. |
| P-037 | 2025-02-02 | Scripts: add repo validator (stdlib) | 1) scripts/validate_repo.py создан. 2) Проверяет наличие ключевых файлов/папок. | scripts/validate_repo.py, PROGRESS.md | ✅ Done | Валидация структуры репо. |
| P-036 | 2025-02-02 | CI: wire link checker into workflow | 1) ci.yml: запуск python scripts/check_links.py. | .github/workflows/ci.yml, PROGRESS.md | ✅ Done | CI проверяет ссылки. |
| P-035 | 2025-02-02 | Scripts: add link checker (stdlib) | 1) scripts/check_links.py создан. 2) Проверяет относительные ссылки на существование файлов. | scripts/check_links.py, PROGRESS.md | ✅ Done | Проверка ссылок в Markdown. |
| P-034 | 2025-02-02 | CI: add basic workflow skeleton | 1) .github/workflows/ci.yml создан. 2) on push/pull_request, checkout, setup-python. | .github/workflows/ci.yml, PROGRESS.md | ✅ Done | Базовый CI. |
| P-033 | 2025-02-02 | Chore: add CODEOWNERS | 1) .github/CODEOWNERS создан. 2) Владелец репо. | .github/CODEOWNERS, PROGRESS.md | ✅ Done | Ответственный за репо. |
| P-032 | 2025-02-02 | Chore: add SUPPORT guidelines | 1) SUPPORT.md создан. 2) Как просить помощи, какие команды/логи приложить. | SUPPORT.md, PROGRESS.md | ✅ Done | Гайд по поддержке. |
| P-031 | 2025-02-02 | Chore: add SECURITY policy | 1) SECURITY.md создан. 2) Как сообщать, что не публиковать. | SECURITY.md, PROGRESS.md | ✅ Done | Политика безопасности. |
| P-030 | 2025-02-02 | Chore: add pull request template | 1) .github/pull_request_template.md создан. 2) Чеклист проверки, как воспроизвести. | .github/pull_request_template.md, PROGRESS.md | ✅ Done | Шаблон PR. |
| P-029 | 2025-02-02 | Chore: configure issue templates | 1) .github/ISSUE_TEMPLATE/config.yml создан. 2) blank issues отключены, ссылки на docs/FAQ. | .github/ISSUE_TEMPLATE/config.yml, PROGRESS.md | ✅ Done | Настройка шаблонов issue. |
| P-028 | 2025-02-02 | Chore: add issue template (feature request) | 1) .github/ISSUE_TEMPLATE/feature_request.md создан. | .github/ISSUE_TEMPLATE/feature_request.md, PROGRESS.md | ✅ Done | Шаблон фичи. |
| P-027 | 2025-02-02 | Chore: add issue template (bug report) | 1) .github/ISSUE_TEMPLATE/bug_report.md создан. | .github/ISSUE_TEMPLATE/bug_report.md, PROGRESS.md | ✅ Done | Шаблон баг-репорта. |
| P-026 | 2025-02-02 | Chore: add gitattributes for line endings | 1) .gitattributes создан. 2) text=auto, eol=lf для md и др. | .gitattributes, PROGRESS.md | ✅ Done | Нормализация переносов строк. |
| P-025 | 2025-02-02 | Chore: improve gitignore for windows and common tooling | 1) .gitignore создан. 2) Windows, IDE, Python/Node, logs, temp. | .gitignore, PROGRESS.md | ✅ Done | Игнор мусора и секретов. |
| P-024 | 2025-02-02 | Chore: add editorconfig | 1) .editorconfig создан. 2) utf-8, eol, trim ws, indent. | .editorconfig, PROGRESS.md | ✅ Done | Единый стиль в редакторах. |
| P-023 | 2025-02-02 | Docs: add CONTRIBUTING guide | 1) CONTRIBUTING.md создан. 2) Ветки/PR, стиль коммитов, локальные проверки, шаблон PR. | CONTRIBUTING.md, PROGRESS.md | ✅ Done | Как вносить вклад. |
| P-022 | 2025-02-02 | Chore: add CODE_OF_CONDUCT | 1) CODE_OF_CONDUCT.md создан. 2) Краткая, структурированная. | CODE_OF_CONDUCT.md, PROGRESS.md | ✅ Done | Правила поведения. |
| P-021 | 2025-02-02 | Docs: mention license and policies in README | 1) README: кратко про LICENSE, CODE_OF_CONDUCT, SECURITY, SUPPORT. | README.md, PROGRESS.md | ✅ Done | Ссылки на политики. |
| P-020 | 2025-02-02 | Chore: add MIT license | 1) LICENSE (MIT) создан. | LICENSE, PROGRESS.md | ✅ Done | Лицензия репо. |
| P-019 | 2025-02-02 | Docs: add CHANGELOG | 1) CHANGELOG.md создан. 2) Unreleased + правила ведения. | CHANGELOG.md, PROGRESS.md | ✅ Done | История изменений. |
| P-018 | 2025-02-02 | Docs: add ROADMAP milestones | 1) ROADMAP.md создан. 2) Этапы и списки задач, реалистичный темп. | ROADMAP.md, PROGRESS.md | ✅ Done | План этапов. |
| P-017 | 2025-02-02 | Docs: improve README structure and navigation | 1) README: секции Цель, Навигация по docs, Прогресс, Как работать. 2) Ссылки на docs и PROGRESS. | README.md, PROGRESS.md | ✅ Done | Главная страница репо. |
| P-016 | 2025-02-02 | Docs: add glossary | 1) docs/GLOSSARY.md создан. 2) Термины: repo/remote/origin/branch/commit/push/PR и др. | docs/GLOSSARY.md, PROGRESS.md | ✅ Done | Единая терминология. |
| P-015 | 2025-02-02 | Docs: add FAQ | 1) docs/FAQ.md создан. 2) 10–12 частых вопросов и короткие ответы. | docs/FAQ.md, PROGRESS.md | ✅ Done | Быстрые ответы на вопросы. |
| P-014 | 2025-02-02 | Docs: add guild verification checklist | 1) docs/12-guild-verify-checklist.md создан. 2) Connect GitHub, verify, что проверять перед verify. | docs/12-guild-verify-checklist.md, PROGRESS.md | ✅ Done | Чеклист верификации. |
| P-013 | 2025-02-02 | Docs: add public commits explanation | 1) docs/11-public-commits-how-counted.md создан. 2) Где смотреть commits/main, public vs private. | docs/11-public-commits-how-counted.md, PROGRESS.md | ✅ Done | Как считаются коммиты. |
| P-012 | 2025-02-02 | Docs: add troubleshooting guide | 1) docs/10-troubleshooting.md создан. 2) upstream, conflicts, auth failed, push rejected. | docs/10-troubleshooting.md, PROGRESS.md | ✅ Done | Решение типовых ошибок. |
| P-011 | 2025-02-02 | Docs: add commit messages style guide | 1) docs/09-commit-messages.md создан. 2) Шаблоны сообщений, плохие vs хорошие примеры. | docs/09-commit-messages.md, PROGRESS.md | ✅ Done | Единый стиль коммитов. |
| P-010 | 2025-02-02 | Docs: add PR workflow guide | 1) docs/08-pr-workflow.md создан. 2) PR, ревью, merge, связка с issue. | docs/08-pr-workflow.md, PROGRESS.md | ✅ Done | Workflow Pull Request. |
| P-009 | 2025-02-02 | Docs: add branching basics guide | 1) docs/07-branches-basics.md создан. 2) Ветки, когда создавать, switch/checkout, safe workflow. | docs/07-branches-basics.md, PROGRESS.md | ✅ Done | Основы веток. |
| P-008 | 2025-02-02 | Docs: add SSH setup guide | 1) docs/06-auth-ssh.md создан. 2) ssh-keygen, добавление ключа, тест подключения. | docs/06-auth-ssh.md, PROGRESS.md | ✅ Done | Подключение по SSH. |
| P-007 | 2025-02-02 | Docs: add authentication via HTTPS guide | 1) docs/05-auth-https-gcm.md создан. 2) Git Credential Manager, 2FA, PAT когда нужен. | docs/05-auth-https-gcm.md, PROGRESS.md | ✅ Done | Вход по HTTPS. |
| P-006 | 2025-02-02 | Docs: add commit conveyor guide | 1) docs/04-commit-conveyor.md создан. 2) status/add/commit/push, как убедиться что коммит публичный. | docs/04-commit-conveyor.md, PROGRESS.md | ✅ Done | Базовый цикл коммитов. |
| P-005 | 2025-02-02 | Docs: add repo creation and clone guide | 1) docs/03-create-and-clone-repo.md создан. 2) Создание public repo, clone HTTPS, типовые ошибки URL 400/404. | docs/03-create-and-clone-repo.md, PROGRESS.md | ✅ Done | Как создать репо и склонировать. |
| P-004 | 2025-02-02 | Docs: add windows git install guide | 1) docs/02-install-git-windows.md создан. 2) Установка Git, проверка, базовая настройка name/email. | docs/02-install-git-windows.md, PROGRESS.md | ✅ Done | Установка Git на Windows. |
| P-003 | 2025-02-02 | Docs: add goal and rules guide | 1) docs/01-goal-and-rules.md создан. 2) Цель — 100 public commits. 3) Запрет на накрутку, как работать безопасно. | docs/01-goal-and-rules.md, PROGRESS.md | ✅ Done | Единое понимание цели и правил. |
| P-002 | 2025-02-02 | Docs: add docs structure and index | 1) docs/README.md — оглавление. 2) docs/_template.md — шаблон гайда (цель/шаги/проверка/ошибки). | docs/README.md, docs/_template.md, PROGRESS.md | ✅ Done | Навигация и единый формат гайдов. |
| P-001 | 2025-02-02 | Docs: add PROGRESS tracker with mini-issue template | 1) Файл PROGRESS.md создан. 2) Таблица с колонками ID/Date/Title/Acceptance criteria/Files changed/Status/Notes. 3) Раздел "How to use" присутствует. 4) Пример одной строки (P-001) заполнен. | PROGRESS.md | ✅ Done | Единая точка учёта прогресса по коммитам. |

## Правила ID

- ID имеют вид **P-001**, **P-002**, … **P-050**.
- Каждый новый коммит получает следующий порядковый номер.
- Строка добавляется **вверху таблицы** (сразу под заголовком).

## How to use

1. **Перед коммитом:** добавь новую строку с новым ID (P-00X). Заполни Title и Acceptance criteria (2–4 проверяемых пункта).
2. **После изменений:** заполни колонку Files changed (список файлов/папок).
3. **Status:** сразу ставь ✅ Done (коммит = выполненная задача).
4. **Notes:** одна строка — зачем это нужно.

Каждый коммит обязан включать изменения в PROGRESS.md.
