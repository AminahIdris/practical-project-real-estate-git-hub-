"""Application settings loaded from environment variables."""

from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Application
    APP_ENV: str = "development"
    APP_SECRET_KEY: str = "replace-me-with-a-strong-secret"
    API_BASE_URL: str = "http://localhost:8000"
    FRONTEND_BASE_URL: str = "http://localhost:3000"

    # Database
    DATABASE_URL: str = "postgresql://app_user:change-me@localhost:5432/real_estate"

    # AI
    AI_PROVIDER: str = "openai"
    AI_API_KEY: str = ""
    AI_MODEL: str = "gpt-4o-mini"

    # n8n
    N8N_BASE_URL: str = "http://localhost:5678"
    N8N_WEBHOOK_SECRET: str = "replace-me"

    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]

    @property
    def is_development(self) -> bool:
        return self.APP_ENV.lower() in ("development", "dev", "local")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
