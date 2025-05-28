from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./ecommerce.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "asjbdbsahfbbfeqbfhjeqehfwuibbBUBUBUWDBBhubeufbHBYBHEABFUbuBFUEAV")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        env_file = ".env"

settings = Settings()