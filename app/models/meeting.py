from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Relationship, Field

from .base import BaseEnum, ModelBase, SchemaBase

if TYPE_CHECKING:
    from .host import Host, HostRead  # noqa: F401
    from .visitor import Visitor, VisitorRead  # Noqa: F401


class MeetingStatus(BaseEnum):
    checked_in = "checked_in"
    checked_out = "checked_out"
    cancelled = "cancelled"


class MeetingBase(ModelBase):
    purpose: str
    check_out_time: Optional[datetime] = Field(default=None, nullable=True)
    status: MeetingStatus = Field(default=MeetingStatus.checked_in)


class Meeting(MeetingBase, table=True):
    """An associate table for hosts and visitors which has a many to many relationship"""

    host_id: int = Field(foreign_key="host.id")
    visitor_id: int = Field(foreign_key="visitor.id")

    # relationships
    host: "Host" = Relationship(back_populates="meetings")
    visitor: "Visitor" = Relationship(back_populates="meetings")


class MeetingCreate(SchemaBase):
    purpose: str
    host_id: int
    visitor_id: int


class MeetingRead(MeetingBase):
    id: int
    host: "HostRead"
    visitor: "VisitorRead"


class MeetingUpdate(SchemaBase):
    purpose: Optional[str] = None
    check_out_time: Optional[datetime] = None
    status: Optional[MeetingStatus] = None
