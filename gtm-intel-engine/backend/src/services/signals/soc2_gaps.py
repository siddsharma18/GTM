from __future__ import annotations

import re
from typing import Any, Dict, List

from ...schemas import Document, Signal


class Soc2GapsDetector:
	name = "soc2_gaps"

	def __init__(self) -> None:
		self.prefilter = re.compile(r"(soc2|audit|control|evidence|pentest|vulnerability)", re.I)

	def detect(self, docs: List[Document], firmo: Dict[str, Any]) -> List[Signal]:
		candidates = [d for d in docs if self.prefilter.search(d.content or "")]
		if not candidates:
			return []
		signals: List[Signal] = []
		for d in candidates[:2]:
			sev = 3 if re.search(r"gap|missing|manual", d.content or "", re.I) else 2
			signals.append(
				Signal(
					account_id=d.account_id,
					type=self.name,
					severity=sev,
					title="SOC2/control gaps hinted",
					description=(d.content or "")[:240],
					raw={"doc_id": d.id, "url": d.url},
				)
			)
		return signals
