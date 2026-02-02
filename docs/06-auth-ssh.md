# Настройка SSH

Как сгенерировать SSH-ключ, добавить его на GitHub и проверить подключение.

## Цель

- SSH-ключ сгенерирован и добавлен в агент (при необходимости).
- Публичный ключ добавлен в аккаунт GitHub.
- Подключение к GitHub по SSH работает (`git clone`/`git push` по SSH URL).

## Шаги

1. **Генерация ключа:**
   ```bash
   ssh-keygen -t ed25519 -C "твой-email@example.com"
   ```
   Можно нажимать Enter (путь и пароль по умолчанию) или задать пароль для ключа.

2. **Запуск ssh-agent и добавление ключа (Windows):**
   ```bash
   Get-Service ssh-agent
   # Если сервис остановлен:
   Start-Service ssh-agent
   ssh-add $env:USERPROFILE\.ssh\id_ed25519
   ```

3. **Копирование публичного ключа:** содержимое файла `~/.ssh/id_ed25519.pub` (можно вывести: `cat ~/.ssh/id_ed25519.pub` или в PowerShell `Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub`).

4. **На GitHub:** Settings → SSH and GPG keys → New SSH key → вставь ключ, сохрани.

5. **Проверка:**
   ```bash
   ssh -T git@github.com
   ```
   Ожидаемый вывод: «Hi username! You've successfully authenticated...».

## Использование

- Клонировать по SSH: `git clone git@github.com:username/repo-name.git`.
- Если репо уже склонирован по HTTPS, можно сменить URL: `git remote set-url origin git@github.com:username/repo-name.git`.

## Типовые ошибки

- **Permission denied (publickey):** ключ не добавлен в агент (`ssh-add`) или не добавлен на GitHub.
- **Host key verification failed:** при первом подключении нужно подтвердить отпечаток хоста (yes).
