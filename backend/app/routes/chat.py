from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils.openai_api import ask_openai
from app.utils.crud import get_messages

router = APIRouter()

class Message(BaseModel):
    message: str
    username: str

@router.post("/send")
async def chat_with_ai(msg: Message):
    try:
        response = ask_openai(prompt=msg.message, username=msg.username)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/messages')
async def fetch_messages(skip: int = 0, limit: int = 100):
    messages = await get_messages(skip=skip, limit=limit)
    return {"messages": messages}
    
