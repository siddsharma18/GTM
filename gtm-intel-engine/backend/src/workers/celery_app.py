from __future__ import annotations

from celery import Celery

from ..settings import settings

celery_app = Celery(
	"gtm_intel_engine",
	broker=settings.REDIS_URL,
	backend=settings.REDIS_URL,
)

celery_app.conf.update(task_serializer="json", result_serializer="json", accept_content=["json"]) 
