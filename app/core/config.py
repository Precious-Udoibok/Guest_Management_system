from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    PROJECT_NAME: str = "Guest Management System"
    SERVER_NAME: str = "localhost"
    SERVER_HOST: str = "http://localhost:8000"
    FIRST_SUPERUSER: str = "admin"
    FIRST_SUPERUSER_PASSWORD: str = ""
    FIRST_SUPERUSER_PHONE: str = ""
    API_V1_STR: str = "/api/v1"

    SECRET_KEY: str = "project_secret_key"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 11520

    USE_SQLITE: bool = True

    SQLITE_DATABASE_URI: str

    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "app"
    DATABASE_URL: str = ""

    DB_DEBUG_MODE: bool = False

    BACKEND_CORS_ORIGINS: list[str] = ["*"]

    class Config:
        env_file = ".env"


settings = Settings()
