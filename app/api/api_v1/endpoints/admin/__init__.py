from fastapi import APIRouter

from app.api.api_v1.endpoints.admin import user, visitor, meeting, staff

router = APIRouter()

# router.include_router(user.router, prefix="/host", tags=["Admin/Users"])
router.include_router(meeting.router, prefix="/meeting", tags=["Admin/Meeting"])
# router.include_router(staff.router, prefix="/staff", tags=["Admin/Staff"])
# router.include_router(visitor.router, prefix="/visitor", tags=["Admin/Visitor"])
