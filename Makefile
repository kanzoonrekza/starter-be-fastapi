-include .env
export

PORT ?= 8000

install:
	uv sync

dev:
	uv run fastapi dev app/main.py --port $(PORT)

run:
	uv run fastapi run app/main.py --port $(PORT)

migration:
	uv run alembic revision --autogenerate -m "$(m)"

migrate:
	uv run alembic upgrade head

rollback:
	uv run alembic downgrade -1

.PHONY: install dev run migration migrate rollback
