import os
from openai import OpenAI
from dotenv import load_dotenv
from app.utils.crud import create_message

load_dotenv()

def ask_openai(prompt: str, username: str, ) -> str:
    client = OpenAI(
        base_url=os.getenv('OPENROUTER_BASE_URL'),
        api_key=os.getenv('OPENROUTER_API_KEY')
    )
    
    completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )
    
    response = create_message(username=username, prompt=prompt, message=completion.choices[0].message.content)
    
    return response