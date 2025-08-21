from __future__ import annotations

from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException, Query

from ..schemas import Document
from ..services.signals.auth_gaps import AuthGapsDetector
from ..services.signals.identity_risks import IdentityRisksDetector
from ..services.signals.hiring_initiatives import HiringInitiativesDetector
from ..services.signals.soc2_gaps import Soc2GapsDetector

router = APIRouter()


@router.post("/run")
def run_signals(account_id: int = Query(...)) -> Dict[str, Any]:
	# For demo, assume documents are from last ingest endpoint and attached to account_id=1
	if account_id != 1:
		raise HTTPException(status_code=404, detail="Account not found in demo")
	# Build mock documents context (would load from DB normally)
	docs = [
		Document(id=1, account_id=1, source="web", url="https://acme.com/security", title="Security", content="We support email/password login; SSO in Enterprise."),
		Document(id=2, account_id=1, source="github", url="https://github.com/acme/app/issues/42", title="Password reset via support", content="Users must email support to reset."),
	]
	firmo = {"size": "mid", "industry": "saas", "tech_stack": {"okta": False}}

	detectors = [AuthGapsDetector(), IdentityRisksDetector(), HiringInitiativesDetector(), Soc2GapsDetector()]
	all_signals = []
	for det in detectors:
		all_signals.extend([s.model_dump() for s in det.detect(docs, firmo)])
	return {"account_id": account_id, "signals": all_signals}


@router.get("/{account_id}")
def get_signals(account_id: int) -> Dict[str, Any]:
	return run_signals(account_id)
