SHELL := /bin/bash

up:
	docker compose up -d --build

down:
	docker compose down -v

fmt:
	cd backend && poetry run black src tests && poetry run isort src tests || true
	cd frontend && pnpm -s prettier -w . || true

test:
	docker compose run --rm backend poetry run pytest -q

seed:
	@echo "Seeding sample domains (acme.com, contoso.com)"
	curl -s -X POST "http://localhost:8000/ingest/account?domain=acme.com" >/dev/null || true
	curl -s -X POST "http://localhost:8000/ingest/account?domain=contoso.com" >/dev/null || true

crawl:
	@if [ -z "$(DOMAIN)" ]; then echo "Usage: make crawl DOMAIN=acme.com"; exit 1; fi
	curl -s -X POST "http://localhost:8000/ingest/account?domain=$(DOMAIN)" | jq .

dev:
	# Backend (uvicorn) + Frontend (vite)
	cd backend && poetry install && poetry run uvicorn src.app:app --reload & \
	cd frontend && pnpm install && pnpm dev

.PHONY: up down fmt test seed crawl dev
