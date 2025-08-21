from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers will be added below
from .routers import health, ingest, signals, score, outreach, alerts, accounts

# GTM impact: Unified API surface for collectors, signals, scoring, outreach, and alerts
app = FastAPI(title="GTM Intel Engine", version="0.1.0")
from starlette.middleware.base import BaseHTTPMiddleware
import uuid


import time
from starlette.middleware.base import BaseHTTPMiddleware

class TimingMiddleware(BaseHTTPMiddleware):
	async def dispatch(self, request, call_next):
		start = time.time()
		resp = await call_next(request)
		elapsed_ms = int((time.time() - start)*1000)
		resp.headers["X-Response-Time-ms"] = str(elapsed_ms)
		return resp

class RequestIDMiddleware(BaseHTTPMiddleware):
	async def dispatch(self, request, call_next):
		req_id = str(uuid.uuid4())
		response = await call_next(request)
		response.headers["X-Request-ID"] = req_id
		return response


app.add_middleware(RequestIDMiddleware)
app.add_middleware(TimingMiddleware)

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(ingest.router, prefix="/ingest", tags=["ingest"])
app.include_router(signals.router, prefix="/signals", tags=["signals"])
app.include_router(score.router, prefix="/score", tags=["score"])
app.include_router(outreach.router, prefix="/outreach", tags=["outreach"])
app.include_router(alerts.router, prefix="/alerts", tags=["alerts"])
app.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
