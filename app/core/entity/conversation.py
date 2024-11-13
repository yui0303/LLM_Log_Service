from datetime import datetime
from typing import List, Dict

from pydantic import BaseModel

class Content(BaseModel):
    type: str
    text: str

    def to_dict(self):
        return {
            "type": self.type,
            "text": self.text
        }

class Message(BaseModel):
    role: str
    content: List[Content]

    def to_dict(self):
        return {
            "role": self.role,
            "content": [content.to_dict() for content in self.content]
        }

class Conversation(BaseModel):
    prompt: List[Message]
    response: str
    time: datetime

    def to_dict(self):
        return {
            "prompt": [message.to_dict() for message in self.prompt],
            "response": self.response,
            "time": self.time
        }

class Conversations(BaseModel):
    id: str
    history: List[Conversation]


