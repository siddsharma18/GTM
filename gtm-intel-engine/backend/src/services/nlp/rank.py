from __future__ import annotations

from typing import List, Tuple

from rank_bm25 import BM25Okapi


def hybrid_rank(query: str, texts: List[str], embeddings: List[List[float]]) -> List[Tuple[int, float]]:
	"""Return indices and scores using simple BM25 + cosine hybrid.

	GTM impact: Better retrieval → higher-quality signals → more relevant outreach.
	"""
	# BM25
	tokens = [t.lower().split() for t in texts]
	bm25 = BM25Okapi(tokens)
	bm_scores = bm25.get_scores(query.lower().split())

	# Cosine similarity on embeddings (assumes normalized-like mock)
	def cosine(a: List[float], b: List[float]) -> float:
		ma = max(1e-9, sum(x * x for x in a) ** 0.5)
		mb = max(1e-9, sum(x * x for x in b) ** 0.5)
		return sum(x * y for x, y in zip(a, b)) / (ma * mb)

	avg_emb = [sum(vals) / len(vals) for vals in zip(*embeddings)] if embeddings else []
	vec_scores = [cosine(e, avg_emb) for e in embeddings] if embeddings else [0.0] * len(texts)

	scores = [(i, 0.6 * bm_scores[i] + 0.4 * vec_scores[i]) for i in range(len(texts))]
	return sorted(scores, key=lambda x: x[1], reverse=True)
