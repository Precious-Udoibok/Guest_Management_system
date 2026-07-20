from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from sqlmodel import Session

from app.api import deps
from app.models import HostRead, HostCreate, Host, HostUpdate
from app.actions import host_action as ha

router = APIRouter()

CommonSession = Annotated[Session, Depends(deps.get_session)]


@router.post("/", response_model=HostRead, status_code=status.HTTP_201_CREATED)
def create_host(session: CommonSession, data: HostCreate) -> Host:
    """
    Endpoint to create a host
    Admin Authentication coming soon...
    """
    host_email = ha.get_by_email(session, email=data.email)
    host_phone = ha.get_by_phone(session, phone=data.phone)
    if host_email:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="A host with this email already exists."
        )
    if host_phone:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="A host with this phone already exists."
        )

    return ha.create(session, data=data)


@router.patch("/{id}", response_model=HostRead)
def update_host(session: CommonSession, id: int, data: HostUpdate) -> Host:
    """
    Update a specific field in the HostUpdate schema by host id
    Authentication Authentication coming soon...
    """
    host = ha.get(session, id)
    if not host:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="This Host does not exist."
        )

    # check email update to avoid duplicate email addresses
    if data.email:
        host_email = ha.get_by_email(session, email=data.email)

        if host_email and host_email.id != id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A host with this email already exists.",
            )

    # Check the phone field to avoid duplicate records
    if data.phone:
        host_phone = ha.get_by_phone(session, phone=data.phone)

        if host_phone and host_phone.id != id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A host with this phone already exists.",
            )

    return ha.update(session, model=host, data=data)


@router.delete("/{id}")
def delete_host(session: CommonSession, id: int):
    """
    Delete a host  by id
    Admin Authentication coming soon...
    """
    host = ha.get(session, id)
    if not host:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="This host doesn't exists."
        )
    ha.delete(session, id)
    return {"message": "Host deleted successfully."}
