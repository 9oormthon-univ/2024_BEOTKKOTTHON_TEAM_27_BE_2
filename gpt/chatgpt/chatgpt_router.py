from fastapi import APIRouter, HTTPException
from openai import OpenAI
import requests
import json

from chatgpt.chatgpt_schema import ChatGPTRequest
from starlette.config import Config

config = Config('chatgpt/.env')
OPENAI_KEY = config('OPENAI_KEY')
MODEL = "gpt-4"

client = OpenAI(
  api_key=OPENAI_KEY,
)
router = APIRouter(
    prefix="/api/gpt/chatgpt",
)


@router.post("")
def get_result(request: ChatGPTRequest):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + OPENAI_KEY
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": request.content
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            response_data = json.loads(response.text)
            content = response_data['choices'][0]['message']['content']
            return {
                "text": content
            }
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))