# GTM (AI GTM Intel Engine)

This repo contains an opinionated, production-grade, demo-ready monorepo that powers an AI-assisted GTM engine (targeting, messaging, delivery). The main project lives under `gtm-intel-engine/`.

For detailed docs, see `gtm-intel-engine/README.md`.

## Quickstart

`bash
# From repo root
cp gtm-intel-engine/.env.example gtm-intel-engine/.env
make -C gtm-intel-engine up
`

Services:
- API docs: http://localhost:8000/docs
- Frontend UI: http://localhost:5173

Seed and demo end-to-end (after services are up):
`bash
make -C gtm-intel-engine seed
curl -s -X POST "http://localhost:8000/ingest/account?domain=acme.com" | jq
curl -s -X POST "http://localhost:8000/signals/run?account_id=1" | jq
curl -s -X POST "http://localhost:8000/score/1" | jq
curl -s -X POST "http://localhost:8000/outreach/1?channel=email" | jq
`

## Local dev (without Docker)
`bash
make -C gtm-intel-engine dev
`
- Backend: Uvicorn on :8000
- Frontend: Vite on :5173

## Environment
Configuration is via  (see `gtm-intel-engine/.env.example`). Common variables:
- `OPENAI_API_KEY` (optional; mock fallback)
- `GITHUB_TOKEN`, `REDDIT_CLIENT_ID`, `REDDIT_SECRET`, `CLEARBIT_KEY` (optional; mock fallbacks)
- `SLACK_WEBHOOK_URL` (optional)

## Testing
`bash
make -C gtm-intel-engine test
`

## Repo hygiene
- `node_modules/` and OS artifacts are ignored and removed from history.
- Add secrets only via environment; never commit them.
