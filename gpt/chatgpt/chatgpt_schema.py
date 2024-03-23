from pydantic import BaseModel


class ChatGPTRequest(BaseModel):
    content: str
