# Mini-Issue Tracker (Progress)

Каждый коммит = одна закрытая mini-issue. Перед коммитом добавляется строка в таблицу, после выполнения — заполняются Files changed, Status = ✅ Done.

## Формат записи

| ID | Date | Title | Acceptance criteria | Files changed | Status | Notes |
|----|------|-------|---------------------|---------------|--------|-------|
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
