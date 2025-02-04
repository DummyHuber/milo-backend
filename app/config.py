import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load environment variables from .env
load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/deepmind")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    LLM_TEMPERATURE: float = os.getenv("LLM_TEMPERATURE", 0.5)
    LLM_HISTORY_LENGTH: int = os.getenv("LLM_HISTORY_LENGTH", 10)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
