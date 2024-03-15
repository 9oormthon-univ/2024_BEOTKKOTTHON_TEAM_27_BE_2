from fastapi import APIRouter, HTTPException
from openai import OpenAI

from .chatgpt_schema import ChatGPTRequest
from starlette.config import Config

config = Config('.env')
OPENAI_KEY = config('OPENAI_KEY')
MODEL = "gpt-3.5-turbo"

client = OpenAI(
  api_key=OPENAI_KEY,
)
router = APIRouter(
    prefix="/api/gpt/chatgpt",
)


@router.post("/result")
def get_result(request: ChatGPTRequest):
    messages = [{"role": "user", "content": request.content}]

    try:
        response = client.completions.create(model=MODEL, prompt=messages)
        return response.choices[0].text
    except Exception as e:
        print(e)
