from sqlmodel import Session, select
from typing import List

from app.models import User, UserCreate, UserUpdate, UserStatus, UserDepartment
from .base import ModelAction


class UserAction(ModelAction[User, UserCreate, UserUpdate]):
    """User CRUD operations"""

    def filter_users(
        self,
        *,
        session: Session,
        status: UserStatus | None = None,
        department: UserDepartment | None = None,
    ) -> List[User]:
        """
        Function to get all users by either status, department or name
        """
        statement = select(User)

        if status:
            statement = statement.where(User.account_status == status)

        if department:
            statement = statement.where(User.department == department)

        return session.exec(statement).all()


user_action = UserAction(User)
