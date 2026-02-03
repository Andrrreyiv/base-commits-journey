# CLI Base Commit Coach

Как пользоваться `tools/base_commit_coach.py` для подсказок по прогрессу.

## Цель

- Быстро узнать число коммитов и записей в PROGRESS.
- Получить напоминание о следующем шаге.

## Команды

- `python tools/base_commit_coach.py --help` — справка.
- `python tools/base_commit_coach.py --report` — число коммитов на HEAD, число записей в PROGRESS.
- `python tools/base_commit_coach.py --next` — подсказка: открыть PROGRESS/ROADMAP и выбрать следующую задачу.

## Требования

- Git в PATH (для --report).
- Запуск из корня репозитория или из любой папки (скрипт находит корень по пути к себе).
