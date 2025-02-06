import json
from dataclasses import asdict
from typing import AsyncGenerator
from fastapi import Request, Depends, APIRouter, HTTPException
from sse_starlette import EventSourceResponse
from starlette.responses import StreamingResponse

from app.dependencies import get_chat_service
from app.schemas import Chat, ChatWithMessage, Message, UserPromptBody
from app.services import ChatService

router = APIRouter()


@router.get(
    "/chats",
    response_model=list[Chat],
    description="Retrieve chat history for the client based on their IP address."
)
async def get_chats(request: Request, llm_service: ChatService = Depends(get_chat_service)):
    """Return the list of available chats."""
    chats = llm_service.get_chats(request.client.host)
    return chats


@router.post(
    "/chat",
    response_model=Message,
    description="Send a new message to create a new chat."
)
async def create_new_chat_with_message(request: Request, body: UserPromptBody, llm_service: ChatService = Depends(get_chat_service)):
    """Handles chat creation when no chat_id is provided."""
    chat = llm_service.create_chat(request.client.host, body.question)
    response = llm_service.send_user_message(chat.id, body)
    return StreamingResponse(response, media_type="text/plain")


@router.get(
    "/chat/{chat_id}",
    response_model=ChatWithMessage,
    description="Get a detailed chat information with the messages."
)
async def get_chat_details(chat_id: int, llm_service: ChatService = Depends(get_chat_service)):
    """Return selected chat with the message history."""
    chat = llm_service.get_chat_by_id(chat_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat cannot be found")
    return chat


@router.post(
    "/chat/{chat_id}",
    response_model=Message,
    description="Send a message in the already created chat."
)
async def send_message(
    chat_id: int,
    body: UserPromptBody,
    llm_service: ChatService = Depends(get_chat_service)
):
    """Handles messages for an existing chat."""
    response = llm_service.send_user_message(chat_id, body)
    return StreamingResponse(response, media_type="text/plain")


@router.delete(
    "/chat/{chat_id}",
    description="Delete selected chat."
)
async def delete_chat(chat_id: int, llm_service: ChatService = Depends(get_chat_service)):
    """Handles deletion of the chat by provided id."""
    return llm_service.delete_chat_by_id(chat_id)
