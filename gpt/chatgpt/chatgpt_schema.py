from pydantic import BaseModel


class ChatGPTRequest(BaseModel):
    system_prompt: str
    content: str
