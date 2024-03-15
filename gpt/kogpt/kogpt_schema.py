from pydantic import BaseModel


class KoGPTRequest(BaseModel):
    content: str
