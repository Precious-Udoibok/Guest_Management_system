# from typing import Optional, List
# from sqlmodel import Session, select

# from app.models import Visitor, VisitorCreate, VisitorUpdate
# from .base import ModelAction


# class VisitorAction(ModelAction[Visitor, VisitorCreate, VisitorUpdate]):
#     """Visitors CRUD operations"""

#     def search(
#         self, session: Session, *, name: Optional[str] = None, email: Optional[str] = None
#     ) -> List[Visitor]:
#         """
#         Return a vistor with the name or email provided
#         """
#         statement = select(Visitor)

#         if name and email:
#             statement = statement.where(
#                 Visitor.name.ilike(f"%{name}%"),
#                 Visitor.email.ilike(f"%{email}%"),
#             )

#         if name:
#             statement = statement.where(Visitor.name.ilike(f"%{name}%"))

#         if email:
#             statement = statement.where(Visitor.email.ilike(f"%{email}%"))

#         return session.exec(statement).all()


# visitor_action = VisitorAction(Visitor)
