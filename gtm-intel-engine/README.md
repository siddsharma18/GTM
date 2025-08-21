# GTM Intel Engine

An opinionated, production-grade, demo-ready monorepo to power an AI-assisted GTM engine that improves targeting, messaging, and delivery. It stitches structured (firmographic/technographic) and unstructured (forums, repos, docs) data into actionable signals, scores accounts, and generates outreach with alerting.

## Why this exists (GTM impact)
- Better targeting → higher reply/conversion by prioritizing right-fit, in-market accounts.
- Better messaging → personalized, credible outreach tied to surfaced risks/opportunities.
- Better delivery → faster SLAs on hot accounts via alerts across channels.

## One-liner
```bash
make up
```
Starts Postgres (pgvector), Redis, API, Celery workers, and the React dashboard.

## Repository layout
```
gtm-intel-engine/
  README.md
  Makefile
  docker-compose.yml
  .env.example
  infra/
    init.sql
  backend/
    pyproject.toml
    src/
      app.py
      settings.py
      db.py
      schemas.py
      deps.py
      routers/
        ingest.py
        score.py
        alerts.py
        outreach.py
        signals.py
        health.py
      services/
        collectors/
          github.py
          reddit.py
          web_docs.py
          clearbit.py
        nlp/
          llm.py
          embed.py
          rank.py
          prompts.py
        scoring/
          feature_builder.py
          account_scorer.py
          rules.yaml
        signals/
          base.py
          auth_gaps.py
          identity_risks.py
          hiring_initiatives.py
          custom_template.py
        outreach/
          templates/
            email.md
            linkedin.md
            call.md
            video.md
          generator.py
        alerts/
          dispatcher.py
      workers/
        celery_app.py
        tasks.py
    tests/
      fixtures/
        firmo.json
        acme_docs.jsonl
        contoso_docs.jsonl
      test_collectors.py
      test_signals.py
      test_scoring.py
      test_outreach.py
  frontend/
    package.json
    tsconfig.json
    vite.config.ts
    index.html
    postcss.config.js
    tailwind.config.js
    src/
      main.tsx
      App.tsx
      lib/api.ts
      components/
        AccountTable.tsx
        AccountDetail.tsx
        InsightChips.tsx
        OutreachPreview.tsx
        ScoreBreakdown.tsx
```

## Quickstart
1) Copy `.env.example` to `.env` and adjust if needed
```bash
cp .env.example .env
```

2) Start everything
```bash
make up
```

3) Seed sample data and run an end-to-end demo
```bash
make seed
# Ingest a sample domain (uses fixtures and deterministic mocks)
curl -s -X POST "http://localhost:8000/ingest/account?domain=acme.com" | jq
# Run signal detectors
curl -s -X POST "http://localhost:8000/signals/run?account_id=1" | jq
# Score account
curl -s -X POST "http://localhost:8000/score/1" | jq
# Generate outreach
curl -s -X POST "http://localhost:8000/outreach/1?channel=email" | jq
# Trigger alerts (console + Slack if configured)
curl -s -X POST "http://localhost:8000/alerts/run" | jq
```

4) Open the dashboard
- Backend API: http://localhost:8000/docs
- Frontend UI: http://localhost:5173

## Local dev without Docker
```bash
make dev
```
- Backend: Poetry + Uvicorn on localhost:8000 (SQLite fallback in tests/dev if `DB_URL` unset)
- Frontend: pnpm + Vite on localhost:5173

## Environment variables (.env)
See `.env.example` for the full list. Important:
- OPENAI_API_KEY (optional; uses deterministic mock if absent)
- REDDIT_CLIENT_ID / REDDIT_SECRET (optional; collectors use mock if absent)
- GITHUB_TOKEN (optional; collectors use unauthenticated or mock)
- SLACK_WEBHOOK_URL (optional)
- DB_URL (defaults to Postgres in Docker; tests/dev can use SQLite)
- REDIS_URL

## Demo script
Paste into your terminal after `make up`:
```bash
# Ingest two accounts using fixtures and mocks
curl -s -X POST "http://localhost:8000/ingest/account?domain=acme.com" | jq
curl -s -X POST "http://localhost:8000/ingest/account?domain=contoso.com" | jq
# Run all signals
curl -s -X POST "http://localhost:8000/signals/run?account_id=1" | jq
curl -s -X POST "http://localhost:8000/signals/run?account_id=2" | jq
# Score
curl -s -X POST "http://localhost:8000/score/1" | jq
curl -s -X POST "http://localhost:8000/score/2" | jq
# Top accounts
curl -s "http://localhost:8000/score/top?n=50" | jq
# Generate outreach for top account
curl -s -X POST "http://localhost:8000/outreach/1?channel=email" | jq
# Trigger alerts
curl -s -X POST "http://localhost:8000/alerts/run" | jq
```

## Make targets
```bash
make up         # Docker compose up (db, redis, api, worker, ui)
make down       # Stop and remove containers
make dev        # Run backend + frontend locally without Docker
make fmt        # Format Python and TypeScript
make test       # Run backend unit tests
make seed       # Seed sample fixtures into DB (or in-memory)
make crawl DOMAIN=acme.com # Run web docs collector for a domain
```

## Modules and GTM impact
- Ingestion (collectors): enriches accounts with public signals → better targeting.
- Signals (detectors): surfaces actionable triggers → sharper messaging.
- Scoring: prioritizes via editable rules → focus on high-propensity accounts.
- Outreach: produces credible, persona-aware assets → higher reply rates.
- Alerts: reduces SLA to engage hot accounts → captures demand.

## Security & compliance
- Respects robots.txt, rate-limited collectors, custom User-Agent `gtm-intel-engine-demo`.
- Stores only public data; fixtures are sanitized; minimal PII.
- Centralized logging with request IDs, meaningful 4xx/5xx.

## Testing
```bash
make test
```
All unit tests run offline using fixtures/mocks.

## Notes
- If `OPENAI_API_KEY` is missing, the LLM and embeddings use deterministic mocks so behavior is reproducible.
- `rules.yaml` governs scoring weights; tweak and re-run `POST /score/{account_id}`.
