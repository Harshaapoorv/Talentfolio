import os
from dotenv import load_dotenv # type: ignore
from pydantic_settings import BaseSettings # type: ignore

# Load .env file from project root (silently does nothing if file missing)
load_dotenv(".env")

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = os.getenv("SQLALCHEMY_DATABASE_URL")
    ENV: str = os.getenv("ENV", "development")
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()