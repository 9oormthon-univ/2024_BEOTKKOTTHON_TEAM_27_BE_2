from fastapi import APIRouter
import config
import requests

from generating.posting_schema import PostingTextRequest, PostingImageRequest
import generating.posting_crud as posting_crud

router = APIRouter(
    prefix="/api/posting",
)

BASE_URL = config.BASE_URL
GPT_PORT = config.GPT_PORT
KOGPT_API = config.KOGPT_API
CHATGPT_API = config.CHATGPT_API


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
    new_image_url = posting_crud.create_image(request.file_name, kogpt_response['text'])

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