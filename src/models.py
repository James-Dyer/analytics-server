from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    recieved_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.current_timestamp(),
    )
    event_type: Mapped[str] = mapped_column(String(32))
    path: Mapped[str] = mapped_column(String(512))
    referrer_host: Mapped[str | None] = mapped_column(String(255))
    session_id: Mapped[str] = mapped_column(String(64))
