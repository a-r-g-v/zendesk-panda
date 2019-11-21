
.PHONY: test
test:
	pipenv run pytest

.PHONY: lint
lint:
	pipenv run mypy
