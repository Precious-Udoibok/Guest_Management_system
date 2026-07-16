from sqlalchemy.engine import Engine
from sqlmodel import SQLModel

# make sure all SQL Alchemy models are imported (app.models) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(engine: Engine, create_tables=False) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, specify True.
    if create_tables:
        SQLModel.metadata.drop_all(engine)  # remove this later
        SQLModel.metadata.create_all(engine)
