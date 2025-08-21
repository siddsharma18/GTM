from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List

from ...schemas import Document, Signal


class SignalDetector(ABC):
	name: str

	@abstractmethod
	def detect(self, docs: List[Document], firmo: Dict[str, Any]) -> List[Signal]:
		"""Return signals from docs + firmo. GTM impact: Actionable triggers drive outreach relevance."""
		raise NotImplementedError
