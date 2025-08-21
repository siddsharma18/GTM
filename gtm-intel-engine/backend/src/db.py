from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import settings


# GTM impact: Reliable persistence enables longitudinal scoring and alert deltas.
engine = create_engine(settings.DB_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


@contextmanager
def get_session() -> Generator:
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()
