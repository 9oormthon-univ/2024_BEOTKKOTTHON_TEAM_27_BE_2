from pydantic import BaseModel


class Store(BaseModel):
    name: str
    address: str


class Promotion(BaseModel):
    channel: str
    type: str
    subject: str
    content: str
    targetGender: str
    targetAge: str


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
    file_name: str


class PostingResponse(BaseModel):
    promotion_text: str
    has_image: bool
    promotion_image_url: str