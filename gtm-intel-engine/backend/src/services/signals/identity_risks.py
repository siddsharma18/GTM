from __future__ import annotations

import re
from typing import Any, Dict, List

from ...schemas import Document, Signal
from ..nlp.embed import Embedder
from ..nlp.rank import hybrid_rank


class IdentityRisksDetector:
	name = "identity_risks"

	def __init__(self) -> None:
		self.embedder = Embedder()
		self.prefilter = re.compile(r"(scim|provisioning|role|audit)", re.I)

	def detect(self, docs: List[Document], firmo: Dict[str, Any]) -> List[Signal]:
		candidates = [d for d in docs if self.prefilter.search(d.content or "")]
		if not candidates:
			return []
		embs = self.embedder.embed_texts([d.content for d in candidates])
		ranked = hybrid_rank("scim role provisioning audit", [d.content for d in candidates], embs)
		signals: List[Signal] = []
		for idx, _ in ranked[:2]:
			d = candidates[idx]
			severity = 3 if re.search(r"manual|absence|lacking", d.content, re.I) else 2
			signals.append(Signal(id=None, account_id=d.account_id, type=self.name, severity=severity, title="Identity provisioning risks", description=d.content[:240], raw={"doc_id": d.id, "url": d.url}))
		return signals
