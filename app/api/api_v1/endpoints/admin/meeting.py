from fastapi import APIRouter, Depends
from typing import Annotated
from sqlmodel import Session

from app.api import deps

router = APIRouter()

CommonSession = Annotated[Session, Depends(deps.get_session)]
