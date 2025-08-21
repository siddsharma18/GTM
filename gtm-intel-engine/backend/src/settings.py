from pydantic_settings import BaseSettings


class Settings(BaseSettings):
	"""Centralized config. GTM impact: Enables safe toggles for mocks vs. live to keep demos deterministic."""
	ENV: str = "local"
	DB_URL: str = "sqlite+pysqlite:///./dev.db"
	REDIS_URL: str = "redis://localhost:6379/0"
	OPENAI_API_KEY: str | None = None
	GITHUB_TOKEN: str | None = None
	REDDIT_CLIENT_ID: str | None = None
	REDDIT_SECRET: str | None = None
	CLEARBIT_KEY: str | None = None
	SLACK_WEBHOOK_URL: str | None = None
	VECTOREMBEDDING_DIM: int = 1536
	ALERT_SCORE_THRESHOLD: int = 70

	class Config:
		env_file = ".env"


settings = Settings()
