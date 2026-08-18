from app.models import Meeting, MeetingCreate, MeetingUpdate
from .base import ModelAction


class MeetingAction(ModelAction[Meeting, MeetingCreate, MeetingUpdate]):
    """Meeting CRUD operations"""

    # def search(
    #     self,
    #     session: Session,
    #     *,
    #     user_id: int | None = None,
    #     status: MeetingStatus | None = None,
    #     search: str | None = None,
    #     offset: int = 0,
    #     limit: int = 100,
    # ) -> List[Meeting]:
    #     """
    #     Return a meeting with the visitor name or email provided
    #     """
    #     statement = select(Meeting)

    #     if user_id:
    #         statement = statement.where(Meeting.user_id == user_id)

    #     if status:
    #         statement = statement.where(Meeting.status == status)

    #     if search:
    #         statement = statement.where(
    #             or_(
    #                 Meeting.visitor_name.ilike(f"%{search}%"),
    #                 Meeting.visitor_email.ilike(f"%{search}%"),
    #                 Meeting.visitor_phone.ilike(f"%{search}%"),
    #             )
    #         )

    #     statement = statement.offset(offset).limit(limit)

    #     return session.exec(statement).all()


meeting_action = MeetingAction(Meeting)
