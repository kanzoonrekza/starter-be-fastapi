"""Settings. Every env var the app reads is a field here — nowhere else."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # extra="ignore": .env also holds non-app vars (PORT is for the Makefile).
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "starter-be-fastapi"
    debug: bool = False


# ponytail: module-level singleton. Swap to a lru_cache'd get_settings()
# dependency only when a test needs to override config per-test.
settings = Settings()
