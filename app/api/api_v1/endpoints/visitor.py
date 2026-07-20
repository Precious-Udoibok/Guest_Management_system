from fastapi import APIRouter, HTTPException, Depends, status
from typing import Annotated
from sqlmodel import Session

from app.actions import visitor_action as va
from app.models import Visitor, VisitorCreate, VisitorRead
from app.api import deps

router = APIRouter()

CommonSession = Annotated[Session, Depends(deps.get_session)]


@router.post("/", response_model=VisitorRead)
def register_visitor(session: CommonSession, data: VisitorCreate) -> Visitor:
    """
    Register a vistor
    """
    visitor_email = va.get_by_email(session, data.email)
    visitor_phone = va.get_by_phone(session, data.phone)

    # validate the visitors email and phone to avoid duplicate records
    if visitor_email:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A visitor with this email address already exists.",
        )
    if visitor_phone:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="A visitor with this phone already exists."
        )

    return va.create(session=session, data=data)
