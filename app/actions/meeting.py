from app.models import Meeting, MeetingCreate, MeetingUpdate
from .base import ModelAction


class MeetingAction(ModelAction[Meeting, MeetingCreate, MeetingUpdate]):
    """For future override of the base CRUD operations"""

    pass


meeting_action = MeetingAction(Meeting)
