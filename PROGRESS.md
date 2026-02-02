# Mini-Issue Tracker (Progress)

Каждый коммит = одна закрытая mini-issue. Перед коммитом добавляется строка в таблицу, после выполнения — заполняются Files changed, Status = ✅ Done.

## Формат записи

| ID | Date | Title | Acceptance criteria | Files changed | Status | Notes |
|----|------|-------|---------------------|---------------|--------|-------|
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
