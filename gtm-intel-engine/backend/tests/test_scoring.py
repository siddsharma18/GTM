from src.services.scoring.account_scorer import score_account


def test_scoring_deterministic():
	firmo = {"size": "enterprise", "industry": "saas", "tech_stack": {"okta": True}}
	signals = [{"type": "auth_gaps", "severity": 4}, {"type": "identity_risks", "severity": 3}]
	docs = [{"crawled_at": None}]
	res = score_account(firmo, signals, docs)
	assert res["fit_score"] > 0
	assert res["intent_score"] > 0
	assert res["total_score"] == res["fit_score"] + res["intent_score"] + res["freshness_score"]
