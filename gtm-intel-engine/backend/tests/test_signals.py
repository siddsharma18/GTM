from src.services.signals.auth_gaps import AuthGapsDetector
from src.services.signals.identity_risks import IdentityRisksDetector
from src.services.signals.hiring_initiatives import HiringInitiativesDetector
from src.schemas import Document


def make_doc(id, content, url="http://x"):  # helper
	return Document(id=id, account_id=1, source="web", url=url, title="t", content=content)


def test_auth_gaps_detector():
	det = AuthGapsDetector()
	docs = [make_doc(1, "We support email+password; SSO later"), make_doc(2, "ok")]
	sigs = det.detect(docs, {"size": "mid"})
	assert any(s.type == "auth_gaps" for s in sigs)


def test_identity_risks_detector():
	det = IdentityRisksDetector()
	docs = [make_doc(1, "SCIM provisioning missing"), make_doc(2, "ok")]
	sigs = det.detect(docs, {})
	assert any(s.type == "identity_risks" for s in sigs)


def test_hiring_detector():
	det = HiringInitiativesDetector()
	docs = [make_doc(1, "Hiring Security Engineer with Okta"), make_doc(2, "ok")]
	sigs = det.detect(docs, {})
	assert any(s.type == "hiring_initiatives" for s in sigs)
