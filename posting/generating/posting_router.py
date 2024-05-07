from fastapi import APIRouter
import os
import requests

from generating.posting_schema import PostingTextRequest, PostingImageRequest
import generating.posting_crud as posting_crud

router = APIRouter(
    prefix="/api/posting",
)

BASE_URL = os.environ.get('BASE_URL')
GPT_PORT = os.environ.get('GPT_PORT')
KOGPT_API = os.environ.get('KOGPT_API')
CHATGPT_API = os.environ.get('CHATGPT_API')


@router.post("/text", status_code=200)
def generate_posting_text(request: PostingTextRequest):
    prompt_message = posting_crud.create_prompt_text(request)
    kogpt_response = request_gpt(GPT_PORT, CHATGPT_API, prompt_message)

    return {
        "posting_text": kogpt_response['text']
    }


@router.post("/image", status_code=200)
def generate_posting_image(request: PostingImageRequest):
    prompt_message = posting_crud.create_prompt_image(request)
    kogpt_response = request_gpt(GPT_PORT, CHATGPT_API, prompt_message)
    new_image_url = posting_crud.create_image(request.file_name, request.promotion.subject, kogpt_response['text'])

    return {
        "new_image_url": new_image_url,
        "kogpt_response": kogpt_response['text']
    }


def request_gpt(gpt_port: str, gpt_api: str, prompt_message: str):
    r = requests.post(
        BASE_URL + gpt_port + gpt_api,
        json={
            "content": prompt_message
        },
        headers={
            'Content-Type': 'application/json'
        }
    )
    print(r)
    return r.json()