from pydantic import BaseModel, Field

class LogConversationRequest(BaseModel):
    conversation_id: str = Field(
        ...,
        title="The conversation id, if not provided, a new conversation_id will be created",
        example=""
    )

class LogConversationResponse(BaseModel):
    conversation_id: str = Field(..., title="The conversation id")
    success: bool = Field(..., title="The log result")

class LogConversationUpdateRequest(BaseModel):
    prompt: str = Field(
        ...,
        title="The conversation prompt. It should be a JSON string. For example: [\{\"type\": \"text\", \"text\": \"Hello\"}]",
        example='[{"role": "user", "content": [{"type": "text", "text": "Hello"}]}]'
    )
    response: str = Field(..., title="The conversation response")

class LogConversationUpdateResponse(BaseModel):
    success: bool = Field(..., title="The update result")