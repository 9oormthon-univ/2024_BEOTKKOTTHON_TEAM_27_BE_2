from fastapi import APIRouter, Request
import config
import requests

from posting_schema import PostingTextRequest, PostingImageRequest
import posting_crud

router = APIRouter(
    prefix="/api/posting",
)

BASE_URL = config.BASE_URL


@router.post("/text", status_code=200)
def generate_posting_text(request: PostingTextRequest):
    print(request)

    prompt_message = posting_crud.create_prompt_text(request)
    kogpt_response = request_kogpt(prompt_message)

    return {
        "posting_text": kogpt_response['text']
    }


@router.post("/image", status_code=200)
def generate_posting_image(request: PostingImageRequest):
    prompt_message = posting_crud.create_prompt_image(request)
    kogpt_response = request_kogpt(prompt_message)
    new_image_url = posting_crud.create_image(request.image_url, kogpt_response['text'])

    return {
        "new_image_url": new_image_url,
        "kogpt_response": kogpt_response['text']
    }


def request_kogpt(prompt_message: str):
    r = requests.post(
        BASE_URL + "/api/kogpt/result",
        json={
            "content": prompt_message
        },
        headers={
            'Content-Type': 'application/json'
        }
    )
    return r.json()
