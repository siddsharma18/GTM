from __future__ import annotations

from typing import Any, Dict, List

from ...schemas import Document, Signal


class CustomTemplateDetector:
	name = "custom_template"

	def detect(self, docs: List[Document], firmo: Dict[str, Any]) -> List[Signal]:
		# Example to add new detector
		return []
