from fastapi import APIRouter

from app.api.api_v1.endpoints import admin, meeting, auth

api_router = APIRouter()

# routes
# api_router.include_router(user.router, prefix="/user", tags=["Users"])
# api_router.include_router(visitor.router, prefix="/visitor", tags=["Visitor"])
api_router.include_router(meeting.router, prefix="/meeting", tags=["Meeting"])
api_router.include_router(auth.router, tags=["Auth"])


# admin routes
api_router.include_router(admin.router, prefix="/admin")
