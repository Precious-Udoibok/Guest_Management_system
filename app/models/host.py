from pydantic import EmailStr
from sqlmodel import Field, Relationship
from typing import Optional, List

from .base import BaseEnum, ModelBase, SchemaBase
from .meeting import Meeting


class HostStatus(BaseEnum):
    available = "available"
    unavailable = "unavailable"


class HostBase(ModelBase):
    name: str
    email: EmailStr
    phone: str
    department: str
    status: HostStatus = Field(default=HostStatus.available)


class Host(HostBase, table=True):
    meetings: List["Meeting"] = Relationship(back_populates="host")


class HostCreate(SchemaBase):
    name: str
    email: EmailStr
    phone: str
    department: str
    status: HostStatus = Field(default=HostStatus.available)


class HostRead(HostBase):
    id: int


class HostUpdate(SchemaBase):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    department: Optional[str] = None
    status: Optional[HostStatus] = None
