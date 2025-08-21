from __future__ import annotations

import json
import os
from typing import Any, Dict

import requests

from ...settings import settings


def dispatch_alert(payload: Dict[str, Any]) -> None:
	severity = payload.get("severity", 0)
	sev_emoji = ":rotating_light:" if severity >= 4 else ":warning:" if severity >= 2 else ":information_source:"
	delta = payload.get("score_delta")
	pre = f"{sev_emoji} "
	"""Send alert to console and Slack (if configured).

	GTM impact: Faster SLAs on hot accounts increase conversion odds.
	"""
	print("[ALERT]", json.dumps(payload))
	url = settings.SLACK_WEBHOOK_URL or os.getenv("SLACK_WEBHOOK_URL")
	if url:
		try:
			requests.post(url, json={"text": f"{pre}GTM Alert: {json.dumps(payload)}"}, timeout=5)
		except Exception:
			pass
