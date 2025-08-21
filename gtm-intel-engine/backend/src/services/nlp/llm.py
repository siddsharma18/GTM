from __future__ import annotations

import json
import random
from typing import Any, Dict, List

from ..nlp import prompts
from ...settings import settings

try:
	from openai import OpenAI  # type: ignore
except Exception:  # pragma: no cover
	OpenAI = None  # type: ignore


class LLMClient:
	"""LLM wrapper with deterministic mock fallback.

	GTM impact: Consistent outputs allow rapid iteration on prompts and messaging without flaky tests.
	"""

	def __init__(self) -> None:
		self.use_mock = not bool(settings.OPENAI_API_KEY)
		if not self.use_mock and OpenAI is not None:
			self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
		else:
			self.client = None

	def summarize_signals(self, company: str, evidence: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
		if self.use_mock or self.client is None:
			# Deterministic mock: derive two signals from evidence keywords
			signals: List[Dict[str, Any]] = []
			joined = " ".join([e.get("snippet", "") for e in evidence]).lower()
			if any(k in joined for k in ["password only", "no sso", "manual reset"]):
				signals.append({
					"type": "auth_gaps",
					"severity": 4,
					"title": f"Potential auth gaps at {company}",
					"description": "Evidence suggests email+password and limited SSO options.",
					"citations": [e.get("url") for e in evidence[:2] if e.get("url")],
				})
			if any(k in joined for k in ["scim", "provisioning", "role"]):
				signals.append({
					"type": "identity_risks",
					"severity": 3,
					"title": "Identity provisioning risk",
					"description": "Hints of manual role provisioning or lacking SCIM.",
					"citations": [e.get("url") for e in evidence[-2:] if e.get("url")],
				})
			return signals or [{
				"type": "hiring_initiatives",
				"severity": 2,
				"title": "Security hiring",
				"description": "Mentions of Security/IAM roles indicate initiatives.",
				"citations": [e.get("url") for e in evidence[:1] if e.get("url")],
			}]

		# Live
		messages = [
			{"role": "system", "content": prompts.SIGNAL_SUMMARIZER_SYSTEM},
			{"role": "user", "content": prompts.SIGNAL_SUMMARIZER_USER.format(company=company, evidence=json.dumps(evidence))},
		]
		resp = self.client.chat.completions.create(model="gpt-4o-mini", messages=messages, temperature=0.2)
		content = resp.choices[0].message.content
		return json.loads(content)

	def write_outreach(self, persona: str, company: str, signals: List[Dict[str, Any]], factors: Dict[str, Any]) -> Dict[str, str]:
		if self.use_mock or self.client is None:
			seed = hash(company + persona) % 1000
			random.seed(seed)
			subject = f"{company} — quick idea on {signals[0]['type'] if signals else 'security posture'}"
			body = (
				f"Hi there,\n\nNoticed {company} {signals[0]['title'].lower() if signals else 'recent security initiatives'}. "
				f"Teams similar to yours reduced risk by {random.choice(["22%","31%","44%"])} after enabling SSO/SCIM. "
				"Worth a 20-min walkthrough to share what good looks like?\n\n— Rep"
			)
			return {"subject": subject, "body": body}

		messages = [
			{"role": "system", "content": prompts.OUTREACH_WRITER_SYSTEM},
			{
				"role": "user",
				"content": prompts.OUTREACH_WRITER_USER.format(
					persona=persona, company=company, signals=json.dumps(signals), factors=json.dumps(factors)
				),
			},
		]
		resp = self.client.chat.completions.create(model="gpt-4o-mini", messages=messages, temperature=0.4)
		content = resp.choices[0].message.content
		return json.loads(content)
