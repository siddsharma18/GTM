from __future__ import annotations

import re
from typing import Any, Dict, List

from ...schemas import Document, Signal


class HiringInitiativesDetector:
	name = "hiring_initiatives"

	def __init__(self) -> None:
		self.prefilter = re.compile(r"(security engineer|iam|soc2|okta|zero trust)", re.I)

	def detect(self, docs: List[Document], firmo: Dict[str, Any]) -> List[Signal]:
		candidates = [d for d in docs if (d.url or "").endswith("/careers") or self.prefilter.search(d.content or "")]
		if not candidates:
			return []
		signals: List[Signal] = []
		for d in candidates[:2]:
			signals.append(Signal(id=None, account_id=d.account_id, type=self.name, severity=2, title="Security/IAM hiring initiative", description=d.content[:240], raw={"doc_id": d.id, "url": d.url}))
		return signals
