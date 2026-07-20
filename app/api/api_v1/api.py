from fastapi import APIRouter

from app.api.api_v1.endpoints import admin, host

api_router = APIRouter()

# routes
api_router.include_router(host.router, prefix="/host", tags=["Host"])

# admin routes
api_router.include_router(admin.router, prefix="/admin")
