import os
from typing import List
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class CORSConfigModel(BaseSettings):
    allow_origins: List[str] = (
        os.getenv("CORS_ALLOW_ORIGINS", "").split(",") if os.getenv("CORS_ALLOW_ORIGINS") else []
    )
    allow_methods: List[str] = (
        os.getenv("CORS_ALLOW_METHODS", "").split(",") if os.getenv("CORS_ALLOW_METHODS") else ["*"]
    )
    allow_headers: List[str] = (
        os.getenv("CORS_ALLOW_HEADERS", "").split(",") if os.getenv("CORS_ALLOW_HEADERS") else ["*"]
    )
    allow_credentials: bool = os.getenv("CORS_ALLOW_CREDENTIALS", "false").lower() == "true"


class Settings(BaseSettings):
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    LLM_TEMPERATURE: float = os.getenv("LLM_TEMPERATURE", 0.5)
    LLM_HISTORY_LENGTH: int = os.getenv("LLM_HISTORY_LENGTH", 10)
    cors: CORSConfigModel = CORSConfigModel()

    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "password")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "deepmind")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "db")
    POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", 5432))
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
