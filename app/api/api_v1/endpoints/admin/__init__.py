from fastapi import APIRouter

from app.api.api_v1.endpoints.admin import host, visitor

router = APIRouter()

router.include_router(host.router, prefix="/host", tags=["Admin/Host"])
router.include_router(visitor.router, prefix="/visitor", tags=["Admin/Visitor"])
