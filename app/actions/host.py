from sqlmodel import Session, select
from typing import List

from app.models import Host, HostCreate, HostUpdate, HostStatus, HostDepartment
from .base import ModelAction


class HostAction(ModelAction[Host, HostCreate, HostUpdate]):
    """Host CRUD operations"""

    def filter_hosts(
        self,
        *,
        session: Session,
        status: HostStatus | None = None,
        department: HostDepartment | None = None,
    ) -> List[Host]:
        """
        Function to get all hosts by either status, department or name
        """
        statement = select(Host)

        if status:
            statement = statement.where(Host.status == status)

        if department:
            statement = statement.where(Host.department == department)

        return session.exec(statement).all()


host_action = HostAction(Host)
