from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter, HTTPException

router = APIRouter()

# Demo in-memory accounts
ACCOUNTS = [
	{"id": 1, "domain": "acme.com", "name": "Acme", "industry": "saas", "size": "mid"},
	{"id": 2, "domain": "contoso.com", "name": "Contoso", "industry": "fintech", "size": "enterprise"},
]


@router.get("")
async def list_accounts() -> Dict[str, Any]:
	return {"accounts": ACCOUNTS}


@router.get("/{account_id}")
async def get_account(account_id: int) -> Dict[str, Any]:
	for a in ACCOUNTS:
		if a["id"] == account_id:
			return {"account": a}
	raise HTTPException(status_code=404, detail="Account not found")
