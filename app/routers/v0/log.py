import os
import json
from dotenv import load_dotenv

from fastapi import APIRouter, HTTPException
from .dtos import LogConversationRequest, LogConversationResponse, LogConversationUpdateRequest, LogConversationUpdateResponse

from app.infra.repositories.mongo.conversations import MongoConversationsRepository
from app.core.entity.conversation import Conversation, Message
from app.core.utils import get_current_time

load_dotenv()

router = APIRouter(prefix="/log", tags=["log"])

mongo_uri = f"mongodb://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PASSWORD')}@{os.getenv('MONGO_HOST')}:{os.getenv('MONGO_PORT')}"

conversations_repo = MongoConversationsRepository(
    mongo_uri=mongo_uri,
    db_name="log_database",
    collection_name="conversations"
)

@router.post("/conversation")
async def conversation(request: LogConversationRequest) -> LogConversationResponse:
    conversation_id_from_req = request.conversation_id
    if conversation_id_from_req == "":
        conversation_id = conversations_repo.create_conversation()
    else:
        conversation_id = conversations_repo.create_conversation(conversation_id_from_req)
    return LogConversationResponse(conversation_id=conversation_id, success=True)

@router.put("/conversation/{conversation_id}")
async def conversation(conversation_id: str, request: LogConversationUpdateRequest) -> LogConversationUpdateResponse:
    try:
        prompt = json.loads(request.prompt)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON format")

    response = request.response
    time = get_current_time()
    message = Conversation(
        prompt=prompt,
        response=response,
        time=time
    )
    success = conversations_repo.append_conversation(conversation_id, message)
    return LogConversationUpdateResponse(success=success)
