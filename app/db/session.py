from sqlmodel import create_engine, Session  # noqa
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

if settings.USE_SQLITE:
    engine = create_engine(
        settings.SQLITE_DATABASE_URI,
        connect_args={"check_same_thread": False},
        pool_pre_ping=True,
        echo=settings.DB_DEBUG_MODE,
    )
else:
    engine = create_engine(
        settings.DATABASE_URL,
        pool_pre_ping=True,
        echo=settings.DB_DEBUG_MODE,
    )

try:
    with engine.connect() as connection:
        logger.info("Database connection successful.")
except Exception as e:
    logger.error(f"Database connection failed: {e}")
    raise
