from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, List


def build_features(firmo: Dict[str, Any], signals: List[Dict[str, Any]], docs: List[Dict[str, Any]]) -> Dict[str, Any]:
	"""Merge firmographics, technographics, recency, and signal density.

	GTM impact: Transparent features align sales intuition with data for trust and adoption.
	"""
	size = firmo.get("size", "mid")
	industry = firmo.get("industry", "other")
	stack = firmo.get("tech_stack", {})

	signal_counts: Dict[str, int] = {}
	severity_sum = 0
	for s in signals:
		signal_counts[s["type"]] = signal_counts.get(s["type"], 0) + 1
		severity_sum += int(s.get("severity", 0))

	fresh_days = 30
	if docs:
		# naive freshness in days
		values = []
	now = datetime.now(timezone.utc)
	for d in docs:
		ts = d.get("crawled_at") or now
		try:
			values.append(max(1, int((now - ts).days)))
		except Exception:
			values.append(fresh_days)
	fresh_days = min([fresh_days] + values)

	return {
		"size": size,
		"industry": industry,
		"tech_okta": bool(stack.get("okta")),
		"tech_aad": bool(stack.get("azure_ad")) or bool(stack.get("aad")),
		"signal_counts": signal_counts,
		"signal_severity_sum": severity_sum,
		"freshness_days": fresh_days,
	}
