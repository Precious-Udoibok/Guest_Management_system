from fastapi import APIRouter, HTTPException, Depends, Query, status
from typing import Annotated
from sqlmodel import Session
from datetime import datetime

from app.actions import meeting_action as ma, user_action as ua
from app.api import deps
from app.models import (
    MeetingRead,
    MeetingCreate,
    UserStatus,
    MeetingStatus,
    AvailabilityStatus,
    MeetingReject,
)

router = APIRouter()

CommonSession = Annotated[Session, Depends(deps.get_session)]


@router.post("/", response_model=MeetingRead)
def create_meeting(session: CommonSession, data: MeetingCreate):
    """
    Create a new meeting
    """
    # check if user exists
    user = ua.get(session, data.user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    # verify staff account is active
    if user.account_status != UserStatus.active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="User account is not active"
        )

    # verify availablity of the user for the meeting
    if user.availability_status != "available":
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="User is not available for the meeting"
        )

    return ma.create(session, data=data)


@router.get("/", response_model=list[MeetingRead])
def get_all_meetings(
    session: CommonSession,
    status: MeetingStatus | None = None,
    search: str | None = None,
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
):
    """
    Get all meetings by status and search
    """
    return ma.search(session=session, status=status, search=search, offset=offset, limit=limit)


@router.get("/staff/{user_id}", response_model=list[MeetingRead])
def get_staff_meetings(
    session: CommonSession,
    user_id: int,
    status: str | None = None,
    search: str | None = None,
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
):
    """
    Authentication coming soon...
    Get all meetings for a specific staff member by user id
    """
    #
    return ma.search(
        session=session, user_id=user_id, status=status, search=search, offset=offset, limit=limit
    )


@router.patch("/{id}/approve", response_model=MeetingRead)
def approve_meeting(session: CommonSession, id: int):
    """
    Authentication coming soon...
    Approve a specific meeting by id
    """
    # check if meeting exists
    meeting = ma.get(session, id)
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")

    if not meeting.status == MeetingStatus.pending:
        raise HTTPException(
            status_code=400, detail="Meeting cannot be approved as it is not in pending status"
        )

    user = meeting.user

    if not user:
        raise HTTPException(status_code=404, detail="Staff member not found")

    if user.availability_status != AvailabilityStatus.available:
        raise HTTPException(
            status_code=409,
            detail="Staff member is no longer available",
        )
    # set meeting status to approve
    updated_meeting = ma.update(session, model=meeting, update={"status": MeetingStatus.ongoing})
    ua.update(session, model=user, update={"availability_status": AvailabilityStatus.busy})

    # notify the guest...
    return updated_meeting


@router.patch("/{id}/reject", response_model=MeetingRead)
def reject_meeting(session: CommonSession, id: int, data: MeetingReject):
    """
    Authentication coming soon...
    Reject a specific meeting by id
    """
    # check if meeting exists
    meeting = ma.get(session, id)
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")

    if not meeting.status == MeetingStatus.pending:
        raise HTTPException(
            status_code=400, detail="Meeting cannot be rejected as it is not in pending status"
        )

    updated_meeting = ma.update(
        session, model=meeting, data=data, update={"status": MeetingStatus.rejected}
    )

    return updated_meeting


@router.patch("/{id}/complete", response_model=MeetingRead)
def complete_meeting(session: CommonSession, id: int):
    """
    Authentication coming soon...
    Complete a specific meeting by id by setting the status to completed
    Toggle the status of the staff to available
    """
    # check if meeting exists
    meeting = ma.get(session, id)

    if not meeting:
        raise HTTPException(status=404, detail="Meeting not found")

    if meeting.status != MeetingStatus.ongoing:
        raise HTTPException(
            status_code=400,
            detail="Meeting cannot be completed in its current status",
        )

    completed_meeting = ma.update(
        session,
        model=meeting,
        update={"status": MeetingStatus.completed, "check_out_time": datetime.now()},
    )

    if meeting.user:
        ua.update(
            session,
            model=meeting.user,
            update={"availability_status": AvailabilityStatus.available},
        )

    return completed_meeting
