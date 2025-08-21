from src.services.outreach.generator import OutreachGenerator


def test_outreach_variants():
	gen = OutreachGenerator()
	variants = gen.generate("Acme", "Security Lead", [{"type": "auth_gaps", "title": "Auth gaps"}], {"size": "mid"}, "email")
	assert len(variants) == 3
	assert all("subject" in v and "body" in v for v in variants)
