from fastapi import HTTPException, Depends

from app.api.deps import get_current_active_account
from app.models import UserRole, User


class RoleCheck:
    def __init__(self, roles: list[UserRole]) -> None:
        self.required_roles = roles

    def __call__(
        self,
        user: User = Depends(get_current_active_account),
    ) -> User:
        if user.role not in self.required_roles:
            raise HTTPException(
                status_code=403,
                detail="Not enough permissions",
            )

        return user
