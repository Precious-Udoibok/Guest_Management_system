from app.models import Visitor, VisitorCreate, VisitorUpdate
from .base import ModelAction


class VisitorAction(ModelAction[Visitor, VisitorCreate, VisitorUpdate]):
    """use for future override of the base CRUD operations"""

    pass


visitor_action = VisitorAction(Visitor)
