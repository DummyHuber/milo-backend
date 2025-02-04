from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime


class UserPromptBody(BaseModel):
    question: str


class Message(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    chat_id: int
    question: str
    response: Optional[str] = None
    created_at: datetime


class Chat(BaseModel):
    id: int
    title: str
    user_ip: str
    created_at: datetime


class ChatWithMessage(Chat):
    messages: List[Message] = []
