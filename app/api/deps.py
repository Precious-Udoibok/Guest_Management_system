from collections.abc import Iterator
from app.db.session import engine, Session


def get_session() -> Iterator[Session]:
    """Access the database"""
    with Session(engine) as session:
        yield session
