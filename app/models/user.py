from pydantic import EmailStr
from sqlmodel import Field, Relationship
from typing import List, TYPE_CHECKING

from .base import BaseEnum, ModelBase, SchemaBase
# from .meeting import Meeting

if TYPE_CHECKING:
    from .meeting import Meeting


class UserRole(BaseEnum):
    admin = "admin"
    staff = "staff"


class UserStatus(BaseEnum):
    active = "active"
    inactive = "inactive"


class AvailabilityStatus(BaseEnum):
    available = "available"
    unavailable = "unavailable"
    busy = "busy"


class UserDepartment(BaseEnum):
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


class UserBase(ModelBase):
    first_name: str
    last_name: str
    email: EmailStr = Field(index=True, unique=True)
    role: UserRole = Field(default=UserRole.staff)
    phone: str = Field(index=True, unique=True)
    password: str
    department: UserDepartment = Field(default=UserDepartment.energy_services)
    availability_status: AvailabilityStatus = Field(default=AvailabilityStatus.available)
    account_status: UserStatus = Field(default=UserStatus.active)


class User(UserBase, table=True):
    meetings: List["Meeting"] = Relationship(back_populates="user")


class UserCreate(SchemaBase):
    first_name: str
    last_name: str
    email: EmailStr = Field(index=True, unique=True)
    role: UserRole = Field(default=UserRole.staff)
    phone: str
    password: str
    department: UserDepartment = Field(default=UserDepartment.energy_services)
    availability_status: AvailabilityStatus = Field(default=AvailabilityStatus.available)
    account_status: UserStatus = Field(default=UserStatus.active)


class UserRead(UserBase):
    id: int


class UserUpdate(SchemaBase):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    role: UserRole | None = None
    phone: str | None = None
    password: str | None = None
    department: UserDepartment | None = None
    availability_status: AvailabilityStatus | None = None
    account_status: UserStatus | None = None
