import os
from dotenv import load_dotenv # type: ignore

# Load .env file from project root (silently does nothing if file missing)
load_dotenv(".env")

class Settings:
    SQLALCHEMY_DATABASE_URL: str = os.getenv("SQLALCHEMY_DATABASE_URL")
    ENV: str = os.getenv("ENV", "development")

settings = Settings()