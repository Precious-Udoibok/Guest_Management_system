from typing import Annotated

from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.api import deps

router = APIRouter()

CommonSession = Annotated[Session, Depends(deps.get_session)]
