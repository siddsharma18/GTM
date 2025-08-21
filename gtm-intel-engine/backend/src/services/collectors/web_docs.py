from __future__ import annotations

from typing import Any, Dict, List


def crawl_site(domain: str) -> List[Dict[str, Any]]:
	"""Mock site crawler combining security/docs/careers/changelog/auth pages.

	GTM impact: First-party docs and careers reveal stack, maturity, and initiatives.
	"""
	base = f"https://{domain}"
	if domain == "acme.com":
		return [
			{"source": "web", "url": base + "/security", "title": "Security", "content": "We support email/password login; SSO in Enterprise."},
			{"source": "web", "url": base + "/careers", "title": "Careers", "content": "Hiring: Security Engineer (IAM, Okta, SOC2)."},
		]
	return [
		{"source": "web", "url": base + "/docs/auth", "title": "Auth", "content": "Password reset via support email; SSO roadmap."}
	]
