from __future__ import annotations

from typing import Any, Dict, List

from .celery_app import celery_app


@celery_app.task
def run_ingest(domain: str) -> Dict[str, Any]:
	# Placeholder task to simulate ingest
	return {"domain": domain, "status": "completed"}
