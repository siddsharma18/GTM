
from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter

from ..services.scoring.account_scorer import score_account

router = APIRouter()


@router.get('/top')
def get_top(n: int = 50) -> Dict[str, Any]:
	# Demo: single account
	return {"accounts": [{"id": 1, "domain": "acme.com", "total_score": post_score(1)["total_score"]}]}


@router.post('/{account_id}')
def post_score(account_id: int) -> Dict[str, Any]:
	if account_id != 1:
		return {"error": "demo supports account_id=1"}
	firmo = {"size": "mid", "industry": "saas", "tech_stack": {"okta": True}}
	signals = [
		{"type": "auth_gaps", "severity": 4},
		{"type": "identity_risks", "severity": 3},
	]
	docs = [
		{"crawled_at": None},
	]
	result = score_account(firmo, signals, docs)
	return {"account_id": account_id, **result}


@router.get('/{account_id}')
def get_score(account_id: int) -> Dict[str, Any]:
	return post_score(account_id)
