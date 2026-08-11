# from fastapi import APIRouter, HTTPException, Depends, status
# from typing import Annotated, List, Optional
# from sqlmodel import Session

# from app.actions import user_action as ha
# from app.models import User, UserRead, UserStatus, UserDepartment
# from app.api import deps


# router = APIRouter()

# CommonSession = Annotated[Session, Depends(deps.get_session)]


# @router.get("/specific/", response_model=List[UserRead])
# def get_all_specific_hosts(
#     session: CommonSession,
#     status: Optional[UserStatus] = None,
#     department: Optional[UserDepartment] = None,
# ):
#     """
#     Get all the specific hosts either by status, department or name
#     """
#     return ha.filter_hosts(session=session, status=status, department=department)


# @router.get("/", response_model=List[UserRead])
# def get_all_hosts(session: CommonSession):
#     """
#     Endpoint to get all the hosts using pagination
#     """
#     return ha.get_all(session)


# @router.get("/{id}", response_model=UserRead)
# def get_host(session: CommonSession, id: int) -> User:
#     """
#     Endpoint to get a host by id
#     """
#     host = ha.get(session, id)
#     if not host:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Host not found")
#     return host
