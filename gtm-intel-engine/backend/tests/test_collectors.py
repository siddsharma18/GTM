from src.services.collectors.github import fetch_github_activity
from src.services.collectors.reddit import search_reddit_mentions
from src.services.collectors.web_docs import crawl_site
from src.services.collectors.clearbit import fetch_firmographics


def test_github_collector():
	docs = fetch_github_activity("acme.com")
	assert any("SSO" in d["title"] for d in docs)


def test_reddit_collector():
	hits = search_reddit_mentions("acme.com", ["sso"]) 
	assert len(hits) >= 1


def test_web_crawler():
	docs = crawl_site("acme.com")
	assert any("Security" in d["title"] for d in docs)


def test_firmo_fixture():
	firmo = fetch_firmographics("acme.com")
	assert firmo["domain"] == "acme.com"
