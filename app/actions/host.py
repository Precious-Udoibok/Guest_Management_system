from sqlmodel import Session, select

from app.models import Host, HostCreate, HostUpdate, HostStatus
from .base import ModelAction


class HostAction(ModelAction[Host, HostCreate, HostUpdate]):
    """use for future override of the base CRUD operations"""

    def filter_hosts(
        self,
        *,
        session: Session,
        status: HostStatus | None = None,
        department: str | None = None,
        name: str | None = None,
    ):
        """
        Function to get all hosts by eiter status, department or name
        """
        statement = select(Host)

        if status:
            statement = statement.where(Host.status == status)

        if department:
            statement = statement.where(Host.department == department)

        if name:
            statement = statement.where(Host.name == name)

        return session.exec(statement).all()


host_action = HostAction(Host)
