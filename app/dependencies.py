from fastapi import Depends
from sqlalchemy.orm import Session, sessionmaker
from app.services import ChatService, LLMService
from app.utils import create_database_engine


def get_db():
    engine = create_database_engine()

    session = engine()
    try:
        yield session
    finally:
        session.close()


def get_chat_service(db: Session = Depends(get_db)):
    """Dependency to provide the LLMService instance."""
    return ChatService(db, llm_service=LLMService())
