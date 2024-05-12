install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

lint:
	poetry run flake8 hexlet_python_package

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

gendiff:
	poetry run python3 /Users/pewspoonmail.ru/python-project-50/gendiff/scripts/gendiff.py

.PHONY: install test lint selfcheck check build

