import json

from sqlalchemy.orm import Session, joinedload
from app.models import Message, Chat
from app.schemas import UserPromptBody
from app.services.llm_service import LLMService
from app.config import settings
from app.utils import DateTimeEncoder


class ChatService:
    def __init__(self, db: Session, llm_service: LLMService):
        """Initialize the service with a database session."""
        self.db = db
        self.llm_service = llm_service
        self.chat_history_limit = settings.LLM_HISTORY_LENGTH

    def get_chats(self, user_ip: str) -> list[Chat] | list:
        """Retrieves all chats."""
        chats = (
            self.db.query(Chat)
            .filter(Chat.user_ip == user_ip)
            .order_by(Chat.created_at.desc())
            .all()
        )
        return chats

    def get_chat_by_id(self, chat_id: int) -> Chat | None:
        """Retrieves a chat by its ID."""
        return (
            self.db.query(Chat)
            .options(joinedload(Chat.messages))
            .filter(Chat.id == chat_id)
            .one_or_none()
        )

    def delete_chat_by_id(self, chat_id: int) -> bool:
        """Deletes a chat by its ID."""
        chat = self.db.query(Chat).filter(Chat.id == chat_id).one_or_none()

        if not chat:
            return False

        self.db.delete(chat)
        self.db.commit()
        return True

    def create_chat(self, user_ip: str, input_text: str):
        """Creates a new chat."""
        chat = Chat(title=input_text, user_ip=user_ip)
        self.db.add(chat)
        self.db.commit()
        self.db.refresh(chat)
        return chat

    def get_messages_by_chat_id(self, chat_id: int, exclude_messages: list[int] | None = None) -> list[Message]:
        """Fetches messages for a chat, excluding specific message IDs."""
        query = (
            self.db.query(Message)
            .filter(Message.chat_id == chat_id)
            .order_by(Message.created_at.asc())
        )

        # Exclude specific messages if exclude_messages is not empty
        if exclude_messages:
            query = query.filter(~Message.id.in_(exclude_messages))

        return query.limit(self.chat_history_limit).all()

    def create_message(self, chat_id: int, input_text: str):
        """Creates a new message entry in the database."""
        message = Message(chat_id=chat_id, question=input_text)
        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)
        return message

    def update_message_response(self, message: Message, response: str):
        """Updates a message with the AI response."""
        message.response = response
        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)
        return message

    def get_llm_response(self, message: Message):
        """Streams response from LLM while updating the database."""
        full_response = ""

        try:
            # Retrieve previous messages from the database
            chat_history = self.get_messages_by_chat_id(message.chat_id, [message.id])

            for chunk in self.llm_service.get_llm_response(message.question, chat_history):
                full_response += chunk
                yield f"chunk||{chunk.strip()}"

            # Update the database after response completes
            message = self.update_message_response(message, full_response)

            #  Yield final message JSON for frontend
            yield "\n"
            yield f"final||{json.dumps({'message': message.to_dict()}, cls=DateTimeEncoder)}"

        except Exception as e:
            yield str(e)

    def send_user_message(self, chat_id: int, body: UserPromptBody):
        message = self.create_message(chat_id, body.question)
        return self.get_llm_response(message)

    def rollback(self):
        """Rollback the session in case of an error."""
        self.db.rollback()

    def close(self):
        """Closes the database session to prevent leaks."""
        self.db.close()
