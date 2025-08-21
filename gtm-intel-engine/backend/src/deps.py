from typing import Generator

from .db import get_session


# Dependency providers for FastAPI

def get_db() -> Generator:
	with get_session() as session:
		yield session
