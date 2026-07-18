from app.models import Host, HostCreate, HostUpdate
from .base import ModelAction


class HostAction(ModelAction[Host, HostCreate, HostUpdate]):
    """use for future override of the base CRUD operations"""

    pass


host_action = HostAction(Host)
