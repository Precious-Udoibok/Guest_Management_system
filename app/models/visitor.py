# from typing import Optional, List, TYPE_CHECKING
# from pydantic import EmailStr
# from sqlmodel import Relationship, Field

# from .base import ModelBase, SchemaBase
# # from .meeting import Meeting

# if TYPE_CHECKING:
#     from .meeting import Meeting


# class VisitorBase(ModelBase):
#     name: str
#     email: EmailStr = Field(index=True, unique=True)
#     phone: str = Field(index=True, unique=True)
#     address: str


# class Visitor(VisitorBase, table=True):
#     meetings: List["Meeting"] = Relationship(back_populates="visitor")


# class VisitorCreate(SchemaBase):
#     name: str
#     email: EmailStr
#     phone: str
#     address: str


# class VisitorRead(VisitorBase):
#     id: int


# class VisitorUpdate(SchemaBase):
#     name: str | None = None
#     email: EmailStr | None = None
#     phone: str | None = None
#     address: str | None = None
