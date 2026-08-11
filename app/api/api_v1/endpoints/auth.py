from fastapi import APIRouter, HTTPException, Depends
from typing import Annotated, Any
from sqlmodel import Session
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm

from app.actions import user_action as ua
from app.api import deps
from app.core.security import verify_password, create_access_token
from app.core.config import settings
from app.models import UserStatus, User
from app.schemas import Token

router = APIRouter()

CommonSession = Annotated[Session, Depends(deps.get_session)]


@router.post("/login", response_model=Token)
def login_user(session: CommonSession, form: OAuth2PasswordRequestForm = Depends()) -> Any:
    """
    Login user using OAuth2 form to get the access token for future requests
    """
    user = ua.get_by_email(session, email=form.username.lower())
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email")

    if not verify_password(form.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect passowrd")

    if user.account_status != UserStatus.active:
        raise HTTPException(status_code=400, detail="Inactive account")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    return {
        "access_token": create_access_token(
            user.id, secret_key=settings.SECRET_KEY, expiry_minutes=access_token_expires
        ),
        "expires": datetime.now() + access_token_expires,
        "token_type": "bearer",
        "account": user,
    }


@router.post("/logout")
def logout(
    current_user: User = Depends(deps.get_current_active_account),
):
    return {"message": "Successfully logged out"}
