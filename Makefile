# Makefile: удобные команды для проверок
# На Windows: если make недоступен, запускай команды вручную (см. ниже)

.PHONY: check links validate hygiene progress

check: links validate hygiene
	@echo "Все проверки пройдены."

links:
	python scripts/check_links.py

validate:
	python scripts/validate_repo.py

hygiene:
	python scripts/check_markdown_hygiene.py

progress:
	python scripts/update_progress.py

# На Windows без make: выполни вручную:
#   python scripts/check_links.py
#   python scripts/validate_repo.py
#   python scripts/check_markdown_hygiene.py
