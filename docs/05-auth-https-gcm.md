# Аутентификация по HTTPS

Как войти в Git при работе по HTTPS: Git Credential Manager, 2FA, когда нужен PAT.

## Цель

- При `git clone` / `git push` по HTTPS запрос логина выполняется один раз (или через сохранённые учётные данные).
- Понимать, когда нужен Personal Access Token (PAT).

## Шаги

1. При первом `git push` или `git clone` приватного репо Windows обычно открывает окно **Git Credential Manager** (GCM).
2. Выбери **Sign in with browser** — откроется браузер, войди в GitHub и разреши доступ.
3. Если у тебя включена **2FA** на GitHub, пароль от аккаунта для Git не подойдёт. Нужен **Personal Access Token (PAT)**:
   - GitHub → Settings → Developer settings → Personal access tokens → Generate new token.
   - Выбери права (минимум `repo` для push/clone).
   - Скопируй токен и вставь его **вместо пароля** в окне GCM или в командной строке при запросе пароля.

## Проверка

- После настройки `git push` выполняется без запроса логина (или один раз запрашивает и запоминает).

## Типовые ошибки

- **Authentication failed:** используй PAT вместо пароля, если включена 2FA.
- **Credential helper не сохраняет:** проверь, что установлен Git for Windows с опцией «Credential Manager»; при необходимости задай: `git config --global credential.helper manager`.
