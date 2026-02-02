# Устранение неполадок

Upstream, конфликты, auth failed, push rejected.

## Цель

- Быстро найти причину типовой ошибки Git/GitHub и исправить.

## Upstream / push rejected

**Ошибка:** `The current branch main has no upstream branch` или `push rejected`.

**Решение:**

- Задать upstream: `git push -u origin main` (один раз).
- Если ветка уже есть на GitHub и ты переименовал локальную: `git push -u origin main` с правильным именем ветки.

## Конфликты при merge/rebase

**Ошибка:** `Merge conflict in файл` или `CONFLICT (content)`.

**Решение:**

1. Открой файл — увидишь маркеры `<<<<<<<`, `=======`, `>>>>>>>`.
2. Оставь нужный вариант (или объедини вручную), удали маркеры.
3. `git add путь/к/файлу`
4. Для merge: `git commit` (сообщение уже подставлено). Для rebase: `git rebase --continue`.

## Authentication failed

**Ошибка:** `Authentication failed` при push/clone по HTTPS.

**Решение:**

- Включена 2FA на GitHub — используй Personal Access Token вместо пароля (см. [Аутентификация по HTTPS](05-auth-https-gcm.md)).
- Проверь: `git remote -v` — URL должен быть правильный; при необходимости обнови учётные данные в Credential Manager (Windows: Панель управления → Учётные данные).

## Push rejected (non-fast-forward)

**Ошибка:** `! [rejected] main -> main (non-fast-forward)`.

**Причина:** На GitHub есть коммиты, которых нет у тебя локально.

**Решение:**

- Подтяни изменения: `git pull --rebase origin main` (или `git pull origin main`), затем `git push`.
- Если уверен, что твоя история верная (осторожно!): `git push --force` — только в своём репо и если понимаешь последствия.

## Другие ошибки

- **fatal: not a git repository:** выполни команду из папки с репозиторием (должна быть подпапка `.git`).
- **Permission denied (publickey):** см. гайд [Настройка SSH](06-auth-ssh.md).
