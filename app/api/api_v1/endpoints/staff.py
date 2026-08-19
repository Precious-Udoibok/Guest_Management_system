from fastapi import APIRouter, Depends
from typing import Annotated
from sqlmodel import Session

from app.api import deps
from app.models import (
    UserRead,
    User,
    UserRole,
    UserDepartment,
)
from app.actions import user_action as ua

router = APIRouter()

CommonSession = Annotated[Session, Depends(deps.get_session)]


@router.get("/", response_model=list[UserRead])
def get_staff(
    session: CommonSession,
    search: str | None = None,
    role: UserRole | None = None,
    department: UserDepartment | None = None,
) -> list[User]:
    """
    get a staff by name or email or department
    """
    search_fields = [
        User.first_name,
        User.last_name,
        User.email,
    ]

    filters = []

    if role:
        filters.append(User.role == role)

    if department:
        filters.append(User.department == department)

    return ua.search(session=session, search=search, search_fields=search_fields, filters=filters)
