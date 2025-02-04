from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings  # Ensure you have settings with DATABASE_URL


def create_database_engine():
    engine = create_engine(settings.DATABASE_URL)

    # Create a SessionLocal class
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)
