from datetime import datetime

from pydantic import BaseModel

from app.models import UserRead


class Token(BaseModel):
    """Token schema for authentication."""

    access_token: str
    token_type: str
    expires: datetime
    account: UserRead


class TokenPayload(BaseModel):
    """Token payload schema for authentication."""

    sub: str | None = None
