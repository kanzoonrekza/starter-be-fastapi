-include .env
export

PORT ?= 8000

install:
	uv sync

dev:
	uv run fastapi dev app/main.py --port $(PORT)

run:
	uv run fastapi run app/main.py --port $(PORT)

.PHONY: install dev run
