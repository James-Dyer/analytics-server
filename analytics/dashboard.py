from flask import Blueprint, current_app, render_template
from sqlalchemy import func, select

from .models import Event

dashboard = Blueprint(
    "dashboard",
    __name__,
    url_prefix="/dashboard",
)


@dashboard.get("/")
def index():
    session_factory = current_app.extensions["session_factory"]

    with session_factory() as session:
        total_views = session.scalar(select(func.count(Event.id))) or 0

        total_sessions = (
            session.scalar(select(func.count(func.distinct(Event.session_id)))) or 0
        )

        latest_event = session.scalar(select(func.max(Event.received_at)))

        page_rows = session.execute(
            select(
                Event.path,
                func.count(Event.id).label("views"),
            )
            .group_by(Event.path)
            .order_by(func.count(Event.id).desc())
        ).all()

    return render_template(
        "dashboard.html",
        total_views=total_views,
        total_sessions=total_sessions,
        latest_event=latest_event,
        page_rows=page_rows,
    )
