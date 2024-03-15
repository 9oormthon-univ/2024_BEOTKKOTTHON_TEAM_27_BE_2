from fastapi import APIRouter, HTTPException
from gpt.chatgpt import config
import openai

from chatgpt_schema import ChatGPTRequest

router = APIRouter(
    prefix="/api/gpt/chatgpt",
)

OPENAI_KEY = config.OPENAI_KEY
MODEL = "gpt-3.5-turbo"

@router.post("/result")
def get_result(request: ChatGPTRequest):
    messages = [{"role": "user", "content": request.content}]
    try:
        response = openai.Completion.create(
            model=MODEL,
            messages=messages,
            temperature=0
        )
        return response.choices[0].message["content"]
    except Exception as e:
        print(e)
