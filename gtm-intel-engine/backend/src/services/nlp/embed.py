from __future__ import annotations

from typing import List

from ...settings import settings

try:
	from openai import OpenAI  # type: ignore
except Exception:  # pragma: no cover
	OpenAI = None  # type: ignore


class Embedder:
	"""Embedding client with mock fallback.

	GTM impact: Deterministic retrieval quality ensures signal accuracy and reproducible scoring.
	"""

	def __init__(self) -> None:
		self.use_mock = not bool(settings.OPENAI_API_KEY)
		if not self.use_mock and OpenAI is not None:
			self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
		else:
			self.client = None

	def embed_texts(self, texts: List[str]) -> List[List[float]]:
		if self.use_mock or self.client is None:
			# Simple hash-based pseudo-embedding with fixed dim
			dim = settings.VECTOREMBEDDING_DIM
			def vec(s: str) -> List[float]:
				seed = abs(hash(s)) % (10**6)
				return [((seed * (i + 1)) % 997) / 997.0 for i in range(dim)]
			return [vec(t) for t in texts]

		resp = self.client.embeddings.create(model="text-embedding-3-large", input=texts)
		return [d.embedding for d in resp.data]
