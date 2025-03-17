from pydantic_settings import BaseSettings
from typing import List
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    # CORS_ORIGINS: List[str]

    class Config:
        env_file = ".env"  # Automatically loads environment variables from .env file

settings = Settings()  # This will load environment variables when the Settings object is instantiated
