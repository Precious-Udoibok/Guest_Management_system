from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.actions import user_action as ua
from app.api import deps, rbac
from app.core.security import get_password_hash
from app.models import (
    User,
    UserDepartment,
    UserOnboard,
    UserProfile,
    UserPublic,
    UserRead,
    UserRole,
)

router = APIRouter()

CommonSession = Annotated[Session, Depends(deps.get_session)]


@router.get("/", response_model=list[UserPublic])
def get_staff(
    session: CommonSession,
    search: str | None = None,
    role: UserRole | None = None,
    department: UserDepartment | None = None,
) -> list[UserPublic]:
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


@router.patch("/onboard", response_model=UserRead)
def staff_onboard(
    session: CommonSession,
    data: UserOnboard,
    authorized: bool = Depends(rbac.RoleCheck([UserRole.staff])),
    current_user: User = Depends(deps.get_current_active_account),  # noqa: B008
) -> User:
    """
    Staff complete Onboarding by updating their firstname, lastname and password
    """
    # check if the staff account has already been onboarded
    current_staff = ua.get(session, id=current_user.id)
    if current_staff.onboarding_completed:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=" This account has already been onboarded."
        )

    update_payload = data.model_dump(exclude={"password"})
    update_payload["hashed_password"] = get_password_hash(data.password)
    update_payload["onboarding_completed"] = True

    return ua.update(session, model=current_staff, update=update_payload)


@router.patch("/profile", response_model=UserRead)
def update_profile(
    session: CommonSession,
    data: UserProfile,
    authorized: bool = Depends(rbac.RoleCheck([UserRole.staff])),
    current_user: User = Depends(deps.get_current_active_account),  # noqa: B008
) -> User:
    """
    Staffs update profile details
    """

    current_staff = ua.get(session, id=current_user.id)
    if not current_staff:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return ua.update(session, model=current_staff, data=data)


@router.get("/profile", response_model=UserRead)
def get_profile(
    session: CommonSession,
    current_user: User = Depends(deps.get_current_active_account),  # noqa: B008
    authorized: bool = Depends(rbac.RoleCheck([UserRole.staff])),
) -> User:
    """
    Get your profile
    """
    profile = ua.get(session, id=current_user.id)
    if not profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return profile
