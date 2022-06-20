import secrets
from typing import Any, Dict, Optional
from pydantic import BaseSettings, PostgresDsn, validator


class AppSettings(BaseSettings):
    APP_HOST: str
    APP_PORT: int
    APP_TITLE: str

    SECRET_KEY: str = secrets.token_urlsafe(256)
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    DB_PORT: str
    DB_HOST: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None
    
    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("DB_USER"),
            password=values.get("DB_PASS"),
            host=values.get("DB_HOST") + ":" + values.get("DB_PORT"),
            path=f"/{values.get('DB_NAME') or ''}",
        )
        
    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = AppSettings()