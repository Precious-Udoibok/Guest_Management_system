from typing import Generic, TypeVar, Optional, Type, List
from pydantic import BaseModel
from sqlmodel import SQLModel, Session, select

ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class ModelAction(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """Base class for CRUD operations."""

    def __init__(self, model: Type[ModelType]):
        self.model = model  # get the model class

    def get(self, session: Session, id: int) -> Optional[ModelType]:
        """
        Retrieve a model instance by its ID.
        """
        return session.get(self.model, id)

    def get_all(self, session: Session) -> List[ModelType]:
        """
        Get all instances of the model.
        """
        return session.exec(select(self.model)).all()

    def get_by_email(self, session: Session, email: str) -> Optional[ModelType]:
        """
        Get a model instance by email
        """
        statement = select(self.model).where(self.model.email == email.lower())
        return session.exec(statement).first()

    def get_by_phone(self, session: Session, phone: str) -> Optional[ModelType]:
        """
        Get a model instance by phone
        """
        statement = select(self.model).where(self.model.phone == phone)
        return session.exec(statement).first()

    def create(self, session: Session, *, data: CreateSchemaType) -> Optional[ModelType]:
        """
        Create a new model instance.
        """

        try:
            pay_load = data.model_dump()
            model = self.model(**pay_load)

            session.add(model)
            session.commit()
            session.refresh(model)

            return model
        except Exception:
            session.rollback()
            raise

    def update(self, session: Session, *, model: ModelType, data: UpdateSchemaType) -> ModelType:
        """
        Update the selected model instance with new data
        """
        try:
            update_data = data.model_dump(exclude_unset=True)

            for key, value in update_data.items():
                setattr(model, key, value)

            session.add(model)
            session.commit()
            session.refresh(model)

            return model
        except Exception:
            session.rollback()
            raise

    def delete(self, session: Session, id: int) -> Optional[ModelType]:
        """
        Delete the selected model instance data by id
        """
        try:
            model = session.get(self.model, id)
            if not model:
                return None
            session.delete(model)
            session.commit()

            return model
        except Exception:
            session.rollback()
            raise
