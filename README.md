# Base Commits Journey

[![CI](https://github.com/Andrrreyiv/base-commits-journey/actions/workflows/ci.yml/badge.svg)](https://github.com/Andrrreyiv/base-commits-journey/actions/workflows/ci.yml)

Репозиторий для пути к 100 публичным коммитам: документация, чеклисты и скрипты.

## Цель

- Достичь **100 публичных коммитов** на default-ветке (`main`) в этом репозитории.
- Вести атомарные коммиты и качественную историю (без накрутки и пустых коммитов).

## Навигация по docs

Вся документация — в папке [docs/](docs/):

- [Оглавление документации](docs/README.md)
- [Цель и правила](docs/01-goal-and-rules.md)
- [Установка Git (Windows)](docs/02-install-git-windows.md)
- [Создание и клонирование репо](docs/03-create-and-clone-repo.md)
- [Конвейер коммитов](docs/04-commit-conveyor.md)
- [Аутентификация HTTPS](docs/05-auth-https-gcm.md)
- [Настройка SSH](docs/06-auth-ssh.md)
- [Ветки](docs/07-branches-basics.md)
- [Pull Request](docs/08-pr-workflow.md)
- [Стиль коммитов](docs/09-commit-messages.md)
- [Устранение неполадок](docs/10-troubleshooting.md)
- [Публичные коммиты](docs/11-public-commits-how-counted.md)
- [Чеклист верификации гильдии](docs/12-guild-verify-checklist.md)
- [FAQ](docs/FAQ.md) · [Глоссарий](docs/GLOSSARY.md)

## Прогресс

- **Mini-issue трекинг:** [PROGRESS.md](PROGRESS.md) — каждая задача = одна строка в таблице.
- **План этапов:** [ROADMAP.md](ROADMAP.md).
- **История изменений:** [CHANGELOG.md](CHANGELOG.md).

## CI

- **Что проверяет:** ссылки в Markdown, наличие ключевых файлов, гигиена Markdown (trailing spaces, финальный перевод строки).
- **Где смотреть логи:** [Actions](https://github.com/Andrrreyiv/base-commits-journey/actions) → workflow **CI**.

## Структура репозитория

```
.
├── docs/           # Документация: гайды 01–14, FAQ, глоссарий
├── scripts/        # Скрипты проверки (Python stdlib): ссылки, валидация, гигиена, прогресс
├── tools/          # CLI: base_commit_coach (--report, --next)
├── .github/        # GitHub: workflows (CI), issue/PR шаблоны, CODEOWNERS, dependabot
├── .vscode/        # Настройки редактора (Cursor/VS Code)
├── README.md       # Главная страница
├── PROGRESS.md     # Mini-issue трекинг
├── ROADMAP.md      # Этапы и задачи
├── CHANGELOG.md    # История изменений
├── LICENSE         # MIT
├── CONTRIBUTING.md # Как вносить вклад
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── SUPPORT.md
├── Makefile        # Команды: check, links, validate, hygiene, progress
├── .editorconfig   # Стиль кода/разметки
├── .gitignore
└── .gitattributes
```

## Как работать

1. Выбери задачу из [PROGRESS.md](PROGRESS.md) или [ROADMAP.md](ROADMAP.md).
2. Добавь строку в PROGRESS.md (если новая задача), сделай изменения, закоммить с понятным сообщением.
3. Каждый коммит должен содержать обновление PROGRESS.md.
4. Регулярно делай `git push`.

## Лицензия и политики

- [LICENSE](LICENSE) (MIT)
- [CODE_OF_CONDUCT](CODE_OF_CONDUCT.md)
- [CONTRIBUTING](CONTRIBUTING.md)
- [SECURITY](SECURITY.md)
- [SUPPORT](SUPPORT.md)

Подробнее см. в указанных файлах.
