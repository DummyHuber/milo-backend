import json
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings  # Ensure you have settings with DATABASE_URL


def create_database_engine():
    engine = create_engine(
        settings.DATABASE_URL,
        pool_recycle=settings.DATABASE_POOL_RECYCLE,
        pool_timeout=settings.DATABASE_POOL_TIMEOUT,
    )

    # Create a SessionLocal class
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.isoformat()
        return super().default(o)
