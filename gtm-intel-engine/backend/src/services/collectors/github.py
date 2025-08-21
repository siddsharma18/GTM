from __future__ import annotations

from typing import Any, Dict, List


def fetch_github_activity(domain: str) -> List[Dict[str, Any]]:
	"""Mock GitHub collector.

	GTM impact: Engineering velocity/changelog signals correlate with change readiness.
	"""
	# Offline deterministic mock: map domain to a couple of commit/issue-like docs
	if domain.endswith("acme.com"):
		return [
			{"source": "github", "url": "https://github.com/acme/app/commit/1", "title": "Add SSO docs", "content": "Okta SSO added; SCIM planned."},
			{"source": "github", "url": "https://github.com/acme/app/issues/42", "title": "Password reset via support", "content": "Users must email support to reset."},
		]
	return [
		{"source": "github", "url": "https://github.com/contoso/app/commit/9", "title": "Auth refactor", "content": "Email+password login; SSO backlog."}
	]
