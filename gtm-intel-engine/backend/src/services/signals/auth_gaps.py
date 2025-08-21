from __future__ import annotations

import re
from typing import Any, Dict, List

from ...schemas import Document, Signal
from ..nlp.embed import Embedder
from ..nlp.rank import hybrid_rank


class AuthGapsDetector:
	name = "auth_gaps"

	def __init__(self) -> None:
		self.embedder = Embedder()
		self.prefilter = re.compile(r"(password only|email\+password|no sso|manual reset)", re.I)

	def detect(self, docs: List[Document], firmo: Dict[str, Any]) -> List[Signal]:
		candidates = [d for d in docs if self.prefilter.search(d.content or "")]
		if not candidates:
			return []
		embs = self.embedder.embed_texts([d.content for d in candidates])
		ranked = hybrid_rank("auth sso scim password", [d.content for d in candidates], embs)
		signals: List[Signal] = []
		for idx, _ in ranked[:2]:
			d = candidates[idx]
			severity = 4 if re.search(r"no sso|password only", d.content, re.I) else 3
			signals.append(Signal(id=None, account_id=d.account_id, type=self.name, severity=severity, title="Authentication gaps detected", description=d.content[:240], raw={"doc_id": d.id, "url": d.url}))
		return signals
