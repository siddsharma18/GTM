from __future__ import annotations

from typing import Any, Dict, List


def search_reddit_mentions(domain: str, keywords: List[str]) -> List[Dict[str, Any]]:
	"""Mock Reddit mentions for keywords.

	GTM impact: External chatter reveals pain and urgency for targeted outreach.
	"""
	kw = ", ".join(keywords)
	if domain == "acme.com":
		return [
			{"source": "reddit", "url": "https://reddit.com/r/saas/comments/abc", "title": "No SSO?", "content": f"Anyone know if acme supports SSO or SCIM? ({kw})"}
		]
	return [
		{"source": "reddit", "url": "https://reddit.com/r/devops/comments/xyz", "title": "Contoso onboarding", "content": f"contoso onboarding is manual; roles tough ({kw})"}
	]
