from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    yookassa_shop_id: Optional[str] = None
    yookassa_api_key: Optional[str] = None

    class Config:
        env_file = ".env"


settings = Settings()