from fastapi import APIRouter

from app.api.api_v1.endpoints import admin, host, visitor

api_router = APIRouter()

# routes
api_router.include_router(host.router, prefix="/host", tags=["Host"])
api_router.include_router(visitor.router, prefix="/visitor", tags=["Visitor"])

# admin routes
api_router.include_router(admin.router, prefix="/admin")
