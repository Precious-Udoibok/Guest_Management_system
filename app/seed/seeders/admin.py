from sqlmodel import Session, select
from app.db.session import engine
from app.models import User, UserRole, AvailabilityStatus, UserStatus, UserDepartment
from app.core.config import settings
from app.core.security import get_password_hash
import logging

logger = logging.getLogger(__name__)


def seed_admin():
    with Session(engine) as session:
        admin_exists = session.exec(
            select(User).where(User.email == settings.FIRST_SUPERUSER)
        ).first()
        if admin_exists:
            logger.info("Admin already exists.")
            return

        admin = User(
            first_name="Admin",
            last_name="User",
            email=settings.FIRST_SUPERUSER,
            phone=settings.FIRST_SUPERUSER_PHONE,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            hashed_password=get_password_hash(settings.FIRST_SUPERUSER_PASSWORD),
            role=UserRole.admin,
            department=UserDepartment.coroperate_operations,
            availability_status=AvailabilityStatus.available,
            account_status=UserStatus.active,
        )
        session.add(admin)
        session.commit()
        logger.info("Admin seeded successfully!")
