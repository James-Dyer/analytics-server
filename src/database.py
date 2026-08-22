from pathlib import Path

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


def init_database(app: Flask) -> None:
    database_path = Path(app.instance_path) / "analytics.db"
    database_url = f"sqlite:///{database_path}"

    engine = create_engine(database_url)
    session_factory = sessionmaker(bind=engine)

    app.extensions["database_engine"] = engine
    app.extensions["session_factory"] = session_factory

    from . import models

    Base.metadata.create_all(engine)
