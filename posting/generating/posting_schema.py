from pydantic import BaseModel


class Store(BaseModel):
    name: str
    address: str


class Promotion(BaseModel):
    category: str
    channel: str
    target: str
    subject: str
    content: str


class PostingTextRequest(BaseModel):
    # store
    store: Store | None = None
    # promotion
    promotion: Promotion | None = None


class PostingImageRequest(BaseModel):
    # store
    store: Store | None = None
    # promotion
    promotion: Promotion | None = None
    # image
    image_url: str


class PostingResponse(BaseModel):
    promotion_text: str
    has_image: bool
    promotion_image_url: str