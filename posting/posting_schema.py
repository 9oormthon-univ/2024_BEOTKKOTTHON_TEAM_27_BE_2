from pydantic import BaseModel

class Store(BaseModel):
    name: str
    address: str

class Promotion(BaseModel):
    type: str
    channel: str
    target: str
    subject: str
    content: str

class PostingTextRequest(BaseModel):
    # store
    store: Store
    # promotion
    promotion: Promotion

class PostingImageRequest(BaseModel):
    # store
    store: Store
    # promotion
    promotion: Promotion
    # image
    image_url: str

class PostingResponse(BaseModel):
    promotion_text: str
    has_image: bool
    promotion_image_url: str