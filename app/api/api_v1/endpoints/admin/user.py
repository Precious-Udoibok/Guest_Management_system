# from fastapi import APIRouter, Depends, HTTPException, status
# from typing import Annotated
# from sqlmodel import Session

# from app.api import deps
# from app.models import UserRead, UserCreate, User, UserUpdate
# from app.actions import user_action as ua

# router = APIRouter()

# CommonSession = Annotated[Session, Depends(deps.get_session)]


# @router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
# def create_user(session: CommonSession, data: UserCreate) -> User:
#     """
#     Endpoint to create a user
#     Admin Authentication coming soon...
#     """
#     user_email = ua.get_by_email(session, email=data.email)
#     user_phone = ua.get_by_phone(session, phone=data.phone)
#     if user_email:
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT, detail="A user with this email already exists."
#         )
#     if user_phone:
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT, detail="A user with this phone already exists."
#         )

#     return ua.create(session, data=data)


# @router.patch("/{id}", response_model=UserRead)
# def update_user(session: CommonSession, id: int, data: UserUpdate) -> User:
#     """
#     Update a specific field in the UserUpdate schema by user id
#     Authentication Authentication coming soon...
#     """
#     user = ua.get(session, id)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="This User does not exist."
#         )

#     # check email update to avoid duplicate email addresses
#     if data.email:
#         user_email = ua.get_by_email(session, email=data.email)

#         if user_email and user_email.id != id:
#             raise HTTPException(
#                 status_code=status.HTTP_409_CONFLICT,
#                 detail="A user with this email already exists.",
#             )

#     # Check the phone field to avoid duplicate records
#     if data.phone:
#         user_phone = ua.get_by_phone(session, phone=data.phone)

#         if user_phone and user_phone.id != id:
#             raise HTTPException(
#                 status_code=status.HTTP_409_CONFLICT,
#                 detail="A user with this phone already exists.",
#             )

#     return ua.update(session, model=user, data=data)


# @router.delete("/{id}")
# def delete_user(session: CommonSession, id: int):
#     """
#     Delete a user  by id
#     Admin Authentication coming soon...
#     """
#     user = ua.get(session, id)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="This user doesn't exists."
#         )
#     ua.delete(session, id)
#     return {"message": "User deleted successfully."}
