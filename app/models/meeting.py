from datetime import datetime
from typing import TYPE_CHECKING
from pydantic import EmailStr

from sqlmodel import Relationship, Field

from .base import BaseEnum, ModelBase, SchemaBase

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class MeetingStatus(BaseEnum):
    pending = "pending"
    rejected = "rejected"
    ongoing = "ongoing"
    completed = "completed"


class MeetingBase(ModelBase):
    user_id: int = Field(foreign_key="user.id")
    visitor_name: str
    visitor_email: EmailStr
    visitor_phone: str
    reason: str
    rejection_reason: str | None = Field(default=None)
    check_out_time: datetime | None = Field(default=None, nullable=True)
    status: MeetingStatus = Field(default=MeetingStatus.pending)


class Meeting(MeetingBase, table=True):
    # relationships
    user: "User" = Relationship(back_populates="meetings")


class MeetingCreate(SchemaBase):
    user_id: int
    visitor_name: str
    visitor_email: EmailStr
    visitor_phone: str
    reason: str


class MeetingRead(MeetingBase):
    id: int


class MeetingUpdate(SchemaBase):
    visitor_name: str | None = None
    visitor_email: EmailStr | None = None
    visitor_phone: str | None = None
    reason: str | None = None
    rejection_reason: str | None = None
    check_out_time: datetime | None = None
    status: MeetingStatus | None = None


class MeetingReject(SchemaBase):
    rejection_reason: str
