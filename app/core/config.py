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
    POSTGRES_PORT: str = "5432"

    DB_DEBUG_MODE: bool = False

    BACKEND_CORS_ORIGINS: list[str] = ["*"]

    SMTP_HOST: str | None = "smtp.gmail.com"
    SMTP_PORT: int | None = 587
    SMTP_USER: str | None = "[EMAIL_ADDRESS]"
    SMTP_PASSWORD: str | None = "123456789"
    EMAILS_FROM_EMAIL: str | None = ""
    EMAILS_ENABLED: bool = True
    SMTP_TLS: bool | None = True
    EMAILS_FROM_NAME: str = "CheckPoint"

    class Config:
        env_file = ".env"


settings = Settings()
