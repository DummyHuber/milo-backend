from sqlalchemy.orm import Session
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from app.promts import prompt
from app.config import settings
from app.models import Message, Chat


class ChatService:
    def __init__(self, db: Session):
        """Initialize the service with a database session."""
        self.db = db

    def get_llm_model(self):
        """Returns an LLM instance."""
        return ChatOpenAI(
            api_key=settings.OPENAI_API_KEY,
            temperature=settings.LLM_TEMPERATURE,
        )

    def create_chat(self, user_ip: str, input_text: str):
        """Creates a new message entry in the database with the user's question."""
        chat = Chat(title=input_text, user_ip=user_ip)
        self.db.add(chat)
        self.db.commit()
        self.db.refresh(chat)
        return chat

    def create_message(self, chat_id: int, input_text: str):
        """Creates a new message entry in the database with the user's question."""
        message = Message(chat_id=chat_id, question=input_text)
        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)
        return message

    def update_message_response(self, message: Message, response: str):
        """Updates a message with the AI response."""
        message.response = response
        self.db.commit()
        self.db.refresh(message)
        return message

    def get_llm_response(self, chat_id: int, input_text: str):
        """Creates a message, queries the AI, and updates the message with the AI response."""
        try:
            # 1️⃣ Store user message
            message = self.create_message(chat_id, input_text)

            # 2️⃣ Get AI response
            llm = self.get_llm_model()
            chain = LLMChain(llm=llm, prompt=prompt)
            response = chain.run({"user_query": input_text})

            # 3️⃣ Update message with response
            return self.update_message_response(message, response)

        except Exception as e:
            self.db.rollback()  # Rollback on failure
            raise e

    def close(self):
        """Closes the database session to prevent leaks."""
        self.db.close()
