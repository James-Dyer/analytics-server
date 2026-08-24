from pathlib import Path

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.engine import make_url
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


def init_database(app: Flask) -> None:
    database_url = app.config["DATABASE_URL"]
    url = make_url(database_url)

    if url.get_backend_name() == "sqlite" and url.database not in (None, ":memory:"):
        Path(url.database).parent.mkdir(parents=True, exist_ok=True)

    engine = create_engine(database_url, connect_args={"timeout": 30})
    session_factory = sessionmaker(bind=engine, expire_on_commit=False)

    app.extensions["database_engine"] = engine
    app.extensions["session_factory"] = session_factory

    from . import models

    Base.metadata.create_all(engine)
