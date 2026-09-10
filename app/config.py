"""Settings. Every env var the app reads is a field here — nowhere else."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "starter-be-fastapi"
    debug: bool = False
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/app"


settings = Settings()
