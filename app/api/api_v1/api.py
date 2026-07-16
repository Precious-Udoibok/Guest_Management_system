from fastapi import APIRouter

from app.api.api_v1.endpoints import admin

api_router = APIRouter()

# routes


# admin routes
api_router.include_router(admin.router, prefix="/admin", tags=["Admin Routes"])
