from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter

from ..services.alerts.dispatcher import dispatch_alert

router = APIRouter()


@router.post("/run")
def run_alerts() -> Dict[str, Any]:
	payload = {"account_id": 1, "trigger": "score_threshold", "score": 85}
	dispatch_alert(payload)
	return {"sent": True}


@router.get("/recent")
def recent_alerts() -> Dict[str, Any]:
	return {"alerts": [{"account_id": 1, "trigger": "score_threshold", "score": 85}]}
