from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, List

from fastapi import APIRouter, Depends, HTTPException, Query

from ..deps import get_db
from ..schemas import Account, BatchIngestRequest, Document
from ..services.collectors.clearbit import fetch_firmographics
from ..services.collectors.github import fetch_github_activity
from ..services.collectors.reddit import search_reddit_mentions
from ..services.collectors.web_docs import crawl_site

router = APIRouter()


@router.post("/account")
def ingest_account(domain: str = Query(...), db=Depends(get_db)) -> Dict[str, Any]:
	# Minimal in-memoryish persistence using DB session placeholder (omitted for brevity)
	firmo = fetch_firmographics(domain)
	docs: List[Dict[str, Any]] = []
	docs += crawl_site(domain)
	docs += fetch_github_activity(domain)
	docs += search_reddit_mentions(domain, ["auth", "sso", "scim", "onboarding", "soc2", "okta", "aad"]) 
	# Attach account_id 1 for demo
	account = {"id": 1, "domain": domain, "name": domain.split(".")[0].title()}
	for d in docs:
		d.update({"account_id": account["id"], "crawled_at": datetime.now(timezone.utc)})
	return {"account": account, "firmographics": firmo, "documents": docs}


@router.post("/batch")
def ingest_batch(payload: BatchIngestRequest) -> Dict[str, Any]:
	return {"accepted": payload.domains, "job_id": "job-1"}


@router.get("/status/{job_id}")
def ingest_status(job_id: str) -> Dict[str, Any]:
	return {"job_id": job_id, "status": "completed", "progress": 1.0}
