from pydantic import BaseModel
from typing import Optional

class ChatMessage(BaseModel):
    user_id: str
    message: str
    timestamp: Optional[str] = None
    prompt: str

class ChatResponse(BaseModel):
    reply: str
