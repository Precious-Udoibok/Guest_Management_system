# from fastapi import APIRouter, HTTPException, status, Depends, Query
# from typing import Annotated, Optional, List, Any
# from sqlmodel import Session

# from app.actions import visitor_action as va
# from app.api import deps
# from app.models import VisitorRead, VisitorUpdate, Visitor

# router = APIRouter()
# CommonSession = Annotated[Session, Depends(deps.get_session)]


# @router.get("/search", response_model=List[VisitorRead])
# def search_visitors(
#     session: CommonSession,
#     name: Optional[str] = Query(default=None),
#     email: Optional[str] = Query(default=None),
# ) -> Visitor:
#     """
#     Search Visitors by name or email
#     """
#     if not name and not email:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Please provide at least one search parameter (name or email).",
#         )
#     return va.search(session, name=name, email=email)


# @router.get("/", response_model=List[VisitorRead])
# def get_all_visitors(session: CommonSession) -> Visitor:
#     """
#     Enspoint to get all visitors
#     """
#     return va.get_all(session)


# @router.get("/{id}", response_model=VisitorRead)
# def get_visitor_by_id(session: CommonSession, id: int) -> Visitor:
#     """
#     Enspoint to get a visitor by ID
#     """
#     visitor = va.get(session, id)
#     if not visitor:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="This visitor does not exists."
#         )
#     return visitor


# @router.patch("/{id}", response_model=VisitorRead)
# def update_visitor(session: CommonSession, id: int, data: Optional[VisitorUpdate]) -> Visitor:
#     """
#     Update a specific field in the VisitorUpdate schema by visitor id
#     Authentication  coming soon...
#     """
#     visitor = va.get(session, id)
#     if not visitor:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="This Visitor does not exist."
#         )

#     # check email update to avoid duplicate email addresses
#     if data.email:
#         visitor_email = va.get_by_email(session, email=data.email)

#         if visitor_email and visitor_email.id != id:
#             raise HTTPException(
#                 status_code=status.HTTP_409_CONFLICT,
#                 detail="A Visitor with this email already exists.",
#             )

#     # Check the phone field to avoid duplicate records
#     if data.phone:
#         visitor_phone = va.get_by_phone(session, phone=data.phone)

#         if visitor_phone and visitor_phone.id != id:
#             raise HTTPException(
#                 status_code=status.HTTP_409_CONFLICT,
#                 detail="A Visitor with this phone already exists.",
#             )

#     return va.update(session, model=visitor, data=data)


# @router.delete("/{id}")
# def delete_visitor(session: CommonSession, id: int) -> Any:
#     """
#     Delete a visitor  by id
#     Admin Authentication coming soon...
#     """
#     visitor = va.get(session, id)
#     if not visitor:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="This visitor doesn't exists."
#         )
#     va.delete(session, id)
#     return {"message": "Visitor deleted successfully."}
