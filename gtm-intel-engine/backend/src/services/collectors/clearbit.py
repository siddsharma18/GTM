from __future__ import annotations

from typing import Any, Dict

from ...settings import settings


def fetch_firmographics(domain: str) -> Dict[str, Any]:
	"""Return firmo/techno data. Uses fixtures if CLEARBIT key absent. 

	GTM impact: Firmo/techno enables better fit scoring and messaging to stack.
	"""
	if not settings.CLEARBIT_KEY:  # signal use of offline fixtures
		from pathlib import Path
		import json

		fixtures = Path(__file__).resolve().parents[3] / "tests" / "fixtures" / "firmo.json"
		data = json.loads(fixtures.read_text())
		return data.get(domain, {"domain": domain, "size": "mid", "industry": "saas", "tech_stack": {}})

	# In a real impl, call Clearbit. Here we return a simple shape for demo.
	return {"domain": domain, "size": "enterprise", "industry": "saas", "tech_stack": {"okta": True}}
