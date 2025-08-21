from __future__ import annotations

import random
from typing import Any, Dict, List

from ..nlp.llm import LLMClient


class OutreachGenerator:
	"""Generate outreach across channels with tone variants.

	GTM impact: Persona-aware, signal-tied outreach increases reply and meeting rates.
	"""

	def __init__(self) -> None:
		self.llm = LLMClient()

	def generate(self, company: str, persona: str, signals: List[Dict[str, Any]], factors: Dict[str, Any], channel: str) -> List[Dict[str, str]]:
		variants: List[Dict[str, str]] = []
		for _ in range(3):
			msg = self.llm.write_outreach(persona=persona, company=company, signals=signals, factors=factors)
			if channel == "linkedin":
				msg = {"subject": "", "body": msg["body"].replace("Hi there,\n\n", "").replace("— Rep", "")}
			variants.append(msg)
		return variants
