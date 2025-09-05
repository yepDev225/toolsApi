from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "Tools Api"
    API_V1_STR: str = "/api/v1"
    ORIGINS:List

    class Config:
        env_file = ".env"

settings = Settings()