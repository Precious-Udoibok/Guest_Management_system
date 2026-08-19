from collections.abc import Iterator
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError


from app.db.session import engine, Session
from app.core.config import settings
from app.models import User, UserStatus
from app.schemas import TokenPayload
from app.core import security

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/login")


def get_session() -> Iterator[Session]:
    """Access the database"""
    with Session(engine) as session:
        yield session


def get_current_account(
    session: Session = Depends(get_session), token: str = Depends(reusable_oauth2)
) -> User:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[security.ALGORITHM])
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(status_code=401, detail="could not validate credentials")

    user = session.get(User, token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="Account not found")

    return user


def get_current_active_account(current_user: User = Depends(get_current_account)) -> User:
    if current_user.account_status != UserStatus.active:
        raise HTTPException(status_code=403, detail="inactive user account")

    return current_user
