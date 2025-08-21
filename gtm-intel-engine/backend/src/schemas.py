from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel


# Pydantic schemas mirror DB tables. GTM impact: clear contract across services and UI.


class Account(BaseModel):
	id: Optional[int]
	domain: str
	name: Optional[str] = None
	industry: Optional[str] = None
	size: Optional[str] = None
	tech_stack: dict[str, Any] = {}
	firmographics: dict[str, Any] = {}
	last_seen_at: Optional[datetime] = None
	created_at: Optional[datetime] = None
	updated_at: Optional[datetime] = None


class Document(BaseModel):
	id: Optional[int]
	account_id: int
	source: Optional[str] = None
	url: Optional[str] = None
	title: Optional[str] = None
	content: str
	text_embedding: Optional[list[float]] = None
	crawled_at: Optional[datetime] = None


class Signal(BaseModel):
	id: Optional[int]
	account_id: int
	type: str
	severity: int
	title: str
	description: str
	raw: dict[str, Any] = {}
	detected_at: Optional[datetime] = None
	source: Optional[str] = None


class Score(BaseModel):
	id: Optional[int]
	account_id: int
	fit_score: int
	intent_score: int
	freshness_score: int
	total_score: int
	factors: dict[str, Any] = {}
	scored_at: Optional[datetime] = None


class Outreach(BaseModel):
	id: Optional[int]
	account_id: int
	channel: str
	subject: Optional[str] = None
	body: Optional[str] = None
	assets: dict[str, Any] = {}
	created_at: Optional[datetime] = None
	status: Optional[str] = None


class Alert(BaseModel):
	id: Optional[int]
	account_id: int
	trigger: str
	payload: dict[str, Any] = {}
	sent_at: Optional[datetime] = None
	channel: Optional[str] = None


class BatchIngestRequest(BaseModel):
	domains: list[str]


class IngestStatus(BaseModel):
	job_id: str
	status: str
	progress: float
