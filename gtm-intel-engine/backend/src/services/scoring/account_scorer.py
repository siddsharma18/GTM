from __future__ import annotations

import math
from pathlib import Path
from typing import Any, Dict

import yaml

from .feature_builder import build_features


def score_account(firmo: Dict[str, Any], signals: list[dict[str, Any]], docs: list[dict[str, Any]]) -> Dict[str, Any]:
	"""Compute fit, intent, freshness, and total based on rules.yaml.

	GTM impact: Deterministic, editable scoring aligns GTM with evolving ICP and plays.
	"""
	rules_path = Path(__file__).resolve().with_name("rules.yaml")
	rules = yaml.safe_load(rules_path.read_text())
	weights = rules["weights"]

	f = build_features(firmo, signals, docs)

	fit = 0
	fit += weights["size"].get(f.get("size"), 0)
	fit += weights["industry"].get(f.get("industry"), 0)
	fit += weights.get("tech_okta", 0) if f.get("tech_okta") else 0
	fit += weights.get("tech_aad", 0) if f.get("tech_aad") else 0

	intent = 0
	intent += f.get("signal_counts", {}).get("auth_gaps", 0) * weights.get("signal_auth_gaps", 0)
	intent += f.get("signal_counts", {}).get("identity_risks", 0) * weights.get("signal_identity_risks", 0)
	intent += f.get("signal_counts", {}).get("hiring_initiatives", 0) * weights.get("hiring_initiatives", 0)

	fresh_half_life = max(1, int(weights.get("freshness_days_half_life", 30)))
	freshness = int(100 * math.exp(-math.log(2) * (f.get("freshness_days", 30) / fresh_half_life)))

	total = int(fit + intent + freshness)

	return {
		"fit_score": int(fit),
		"intent_score": int(intent),
		"freshness_score": int(freshness),
		"total_score": total,
		"factors": f,
	}
