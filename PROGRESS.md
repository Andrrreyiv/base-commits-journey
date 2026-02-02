# Mini-Issue Tracker (Progress)

Каждый коммит = одна закрытая mini-issue. Перед коммитом добавляется строка в таблицу, после выполнения — заполняются Files changed, Status = ✅ Done.

## Формат записи

| ID | Date | Title | Acceptance criteria | Files changed | Status | Notes |
|----|------|-------|---------------------|---------------|--------|-------|
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
