from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from sqlmodel import Session

from app.api import deps, rbac
from app.core.security import generate_random_password, get_password_hash
from app.models import (
    UserRead,
    User,
    UserStaffCreate,
    UserRole,
    UserStatus,
)
from app.actions import user_action as ua

router = APIRouter()

CommonSession = Annotated[Session, Depends(deps.get_session)]


# Create staff
@router.post("/", response_model=UserRead)
def register_staff(
    session: CommonSession,
    data: UserStaffCreate,
    authorized: bool = Depends(rbac.RoleCheck([UserRole.admin])),
    current_user: User = Depends(deps.get_current_active_account),
):
    """
    Register a staff
    """
    existing_staff = ua.get_by_email(session, email=data.email)
    if existing_staff:
        raise HTTPException(status_code=400, detail="This email address already exists")

    # password
    generated_password = generate_random_password(10)

    new_staff = ua.create(session, data=data)

    return ua.update(
        session=session,
        model=new_staff,
        update={
            "role": UserRole.staff,
            "hashed_password": get_password_hash(generated_password),
        },
    )


@router.post("/{staff_id}/reset-password", response_model=UserRead)
def reset_password(
    session: CommonSession,
    staff_id: int,
    authorized: bool = Depends(rbac.RoleCheck([UserRole.admin])),
    current_user: User = Depends(deps.get_current_active_account),
):
    """
    Reset a staff password
    Email configuration coming soon...
    """
    existing_staff = ua.get(session, id=staff_id)
    if not existing_staff:
        raise HTTPException(status_code=404, detail="This staff does not exist in the system")

    if existing_staff.role != UserRole.staff:
        raise HTTPException(status_code=400, detail="This user is not a staff")

    # password
    generated_password = generate_random_password(10)

    # send the newpassword to their email

    return ua.update(
        session=session,
        model=existing_staff,
        update={
            "hashed_password": get_password_hash(generated_password),
        },
    )

    # return {"message": "Staff password has been reset successfully"}


@router.post("/{staff_id}/disable", response_model=UserRead)
def disable_account(
    session: CommonSession,
    staff_id: int,
    authorized: bool = Depends(rbac.RoleCheck([UserRole.admin])),
    current_user: User = Depends(deps.get_current_active_account),
):
    """
    Disable a staff account
    """
    staff = ua.get(session, id=staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="This staff does not exist in the system")

    if staff.account_status == UserStatus.inactive:
        raise HTTPException(status_code=400, detail="The account is already disabled")

    if staff.role != UserRole.staff:
        raise HTTPException(status_code=400, detail="This user is not a staff")

    return ua.update(session=session, model=staff, update={"account_status": UserStatus.inactive})


@router.post("/{staff_id}/enable", response_model=UserRead)
def enable_account(
    session: CommonSession,
    staff_id: int,
    authorized: bool = Depends(rbac.RoleCheck([UserRole.admin])),
    current_user: User = Depends(deps.get_current_active_account),
):
    """
    Enable a staff account
    """
    staff = ua.get(session, id=staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="This staff does not exist in the system")

    if staff.account_status == UserStatus.active:
        raise HTTPException(status_code=400, detail="The account is already enabled")

    if staff.role != UserRole.staff:
        raise HTTPException(status_code=400, detail="This user is not a staff")

    return ua.update(session=session, model=staff, update={"account_status": UserStatus.active})


# @router.get("/")
# def get_all_staffs(session: CommonSession):
#     """
#     Get all staffs
#     """
#     pass


# @router.get("/")
# def get_all_staffs(session: CommonSession):
#     """
#     Get all staffs
#     """
#     pass
