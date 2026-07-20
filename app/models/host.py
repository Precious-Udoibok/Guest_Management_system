from pydantic import EmailStr
from sqlmodel import Field, Relationship
from typing import Optional, List

from .base import BaseEnum, ModelBase, SchemaBase
from .meeting import Meeting


class HostStatus(BaseEnum):
    available = "available"
    unavailable = "unavailable"


class HostDepartment(BaseEnum):
    energy_services = "energy_services"
    digital_services = "digital_services"
    learning_services = "learning_services"
    innovation_services = "innovation_services"
    coroperate_finance = "coroperate_finance"
    coroperate_operations = "coroperate_innovation"
    human_resouce = "human_resource"
    business_locations = "business_locations"
    technology_innovation = "technology_innovation"
    marketing_communication = "marketing_communication"


class HostBase(ModelBase):
    name: str
    email: EmailStr = Field(index=True, unique=True)
    phone: str = Field(index=True, unique=True)
    department: HostDepartment
    status: HostStatus = Field(default=HostStatus.available)


class Host(HostBase, table=True):
    meetings: List["Meeting"] = Relationship(back_populates="host")


class HostCreate(SchemaBase):
    name: str
    email: EmailStr
    phone: str
    department: HostDepartment
    status: HostStatus = Field(default=HostStatus.available)


class HostRead(HostBase):
    id: int


class HostUpdate(SchemaBase):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    department: Optional[HostDepartment] = None
    status: Optional[HostStatus] = None
