import enum
import random
from sqlmodel import SQLModel, text, func, Field
from typing import Optional
from datetime import datetime


class SchemaBase(SQLModel):
    class Config:
        use_enum_values = True


class ModelBase(SchemaBase):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: Optional[datetime] = Field(
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP")}, nullable=False
    )
    updated_at: Optional[datetime] = Field(
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP"), "onupdate": func.now()},
        nullable=False,
    )


class BaseEnum(str, enum.Enum):  # Inherit from `str` to make it JSON serializable
    def __str__(self):
        return self.value  # Ensures JSON responses return string values

    # for writing tests
    @classmethod
    def random(cls):
        """Return a random enum value from the subclass."""
        return random.choice(list(cls))
