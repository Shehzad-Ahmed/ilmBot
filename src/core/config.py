from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "ilmBot API"
    ENV: str = "development"
    OPENROUTER_API_BASE_URL: str
    OPENROUTER_API_KEY: str
    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()
