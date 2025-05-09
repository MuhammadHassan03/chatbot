from fastapi import Depends
from datetime import datetime
from app.db.supabase import get_supabase_client
from supabase import Client


def create_message(username: str, message: str, prompt):
    supabase: Client = get_supabase_client()

    response = supabase.table('messages').insert({
        "username": username,
        "message": message,
        "prompt": prompt,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }).execute()
    
    return response.data

async def get_messages(skip: int = 0, limit: int = 100):
    supabase: Client = get_supabase_client()
    messages = supabase.table('messages').select("*").range(skip, skip + limit - 1).execute()
    return messages.data
