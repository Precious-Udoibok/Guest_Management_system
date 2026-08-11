import enum
import random
from sqlmodel import SQLModel, text, func, Field
from datetime import datetime
from pydantic import ConfigDict


class SchemaBase(SQLModel):
    model_config = ConfigDict(
        from_attributes=True, use_enum_values=True, coerce_numbers_to_str=True
    )


class ModelBase(SchemaBase):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime | None = Field(
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP")},
        nullable=False,
        # default=None
    )
    updated_at: datetime | None = Field(
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP"), "onupdate": func.now()},
        nullable=False,
        # default=None,
    )


class BaseEnum(str, enum.Enum):  # Inherit from `str` to make it JSON serializable
    def __str__(self):
        return self.value  # Ensures JSON responses return string values

    # for writing tests
    @classmethod
    def random(cls):
        """Return a random enum value from the subclass."""
        return random.choice(list(cls))
