# Установка Git (Windows)

Как установить Git на Windows и проверить, что он работает.

## Цель

- Git установлен и доступен в терминале.
- Настроены имя и email для коммитов.

## Шаги

1. Скачай установщик: [git-scm.com/download/win](https://git-scm.com/download/win).
2. Запусти установщик. Рекомендуется оставить опции по умолчанию (в т.ч. «Git from the command line»).
3. После установки открой новый терминал (PowerShell или cmd) и выполни:
   ```bash
   git --version
   ```
   Должна появиться строка вида `git version 2.x.x`.
4. Настрой имя и email (обязательно для коммитов):
   ```bash
   git config --global user.name "Твоё Имя"
   git config --global user.email "email@example.com"
   ```
   Email лучше указать тот, что привязан к аккаунту GitHub.

## Проверка

- `git --version` — выводит версию.
- `git config --global --get user.name` и `git config --global --get user.email` — выводят заданные имя и email.

## Типовые ошибки

- **«git не распознаётся»:** перезапусти терминал или добавь путь Git в PATH вручную (обычно `C:\Program Files\Git\cmd`).
- **Коммит без name/email:** Git выдаст ошибку — выполни команды из шага 4.
