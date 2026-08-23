from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


def init_database(app: Flask) -> None:
    engine = create_engine(app.config["DATABASE_URL"])
    session_factory = sessionmaker(bind=engine)

    app.extensions["database_engine"] = engine
    app.extensions["session_factory"] = session_factory

    from . import models

    Base.metadata.create_all(engine)
