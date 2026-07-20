from typing import Optional, List
from pydantic import EmailStr
from sqlmodel import Relationship, Field

from .base import ModelBase, SchemaBase
from .meeting import Meeting


class VisitorBase(ModelBase):
    name: str
    email: EmailStr = Field(index=True, unique=True)
    phone: str = Field(index=True, unique=True)
    address: str


class Visitor(VisitorBase, table=True):
    meetings: List["Meeting"] = Relationship(back_populates="visitor")


class VisitorCreate(SchemaBase):
    name: str
    email: EmailStr
    phone: str
    address: str


class VisitorRead(VisitorBase):
    id: int


class VisitorUpdate(SchemaBase):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None
