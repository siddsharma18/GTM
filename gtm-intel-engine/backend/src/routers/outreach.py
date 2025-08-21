from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter, HTTPException

from ..services.outreach.generator import OutreachGenerator

router = APIRouter()

gen = OutreachGenerator()


@router.post("/{account_id}")
def generate_outreach(account_id: int, channel: str = "email") -> Dict[str, Any]:
	if account_id != 1:
		raise HTTPException(status_code=404, detail="Account not found in demo")
	company = "Acme"
	persona = "Security Lead"
	signals = [
		{"type": "auth_gaps", "title": "Authentication gaps detected"},
	]
	factors = {"size": "mid", "industry": "saas"}
	return {"account_id": account_id, "channel": channel, "variants": gen.generate(company, persona, signals, factors, channel)}


@router.get("/{account_id}")
def get_outreach(account_id: int) -> Dict[str, Any]:
	return generate_outreach(account_id)
