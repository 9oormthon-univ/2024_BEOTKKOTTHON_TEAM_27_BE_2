from pillow_heif import register_heif_opener
from PIL import Image
from io import BytesIO
import requests
import config

from generating.posting_schema import PostingTextRequest, PostingImageRequest
from editing.edit_image import put_text_on_image
from generating.prompt import *

font_list = ['WAGURI-TTF.ttf', 'DNFBitBitv2.ttf', 'goryung-strawberry.ttf', 'SDSamliphopangcheTTFOutline.ttf', 'Jalnan2TTF.ttf', 'KakaoBold.ttf']


def get_system_prompt():
    return '''당신은 SNS 마케팅 담당자입니다.
    '가게 이름', '가게 주소', '홍보 주제', '홍보 채널', '홍보 대상', '강조할 내용'을 보고 자연스러운 홍보글을 센스있게 작성해주세요. 단 홍보 대상은 글에 절대 포함하지 말고, 글 스타일을 결정할 때만 참고해주세요..'''


def create_prompt_text(request: PostingTextRequest):
    prompt_message_primary = get_prompt_example(request.promotion.channel)
    prompt_message = f"가게 이름: {request.store.name} \
                    가게 주소: {request.store.address} \
                    홍보 주제: {request.promotion.subject} \
                    홍보 채널: {request.promotion.channel} \
                    홍보 대상: {request.promotion.targetAge} + {request.promotion.targetGender} \
                    강조할 내용: {request.promotion.content} \
                    답변:"
    return prompt_message_primary + prompt_message


def get_prompt_example(promotion_channel: str):
    if promotion_channel == '인스타그램':
        return instagram_example
    elif promotion_channel == '당근마켓':
        return dangn_example
    elif promotion_channel == '카카오톡 채널' or promotion_channel == '카카오톡 동네소식':
        return kakaotalk


def create_prompt_image(request: PostingImageRequest):
    prompt_message = f"가게 이름: {request.store.name} \
                    가게 주소: {request.store.address} \
                    홍보 주제: {request.promotion.subject} \
                    홍보 채널: {request.promotion.channel} \
                    홍보 대상: {request.promotion.targetAge} + {request.promotion.targetGender} \
                    강조할 내용: {request.promotion.content} \
                    해시태그: "
    return prompt_message


def create_image(file_name: str, subject: str, text: str):
    image_data = get_ibm_object(file_name.split('.')[0], '.' + file_name.split('.')[1])

    if file_name.split('.')[1] == 'heic':
        register_heif_opener()
    image = Image.open(image_data)

    # new_image = put_text_on_image(image, subject, text, "font/" + random.choice(font_list), "white")
    new_image = put_text_on_image(image, subject, text, "font/SDSamliphopangcheTTFOutline.ttf", "white", "editing/logo/logo4.png", (130, 90))

    if new_image.mode == 'RGBA':
        new_image = new_image.convert('RGB')

    buffer = BytesIO()
    new_image.save(buffer, format="JPEG")
    new_file_name = put_ibm_object(buffer.getvalue(), '.jpeg')
    return new_file_name


def get_ibm_object(file_name: str, file_extension: str):
    url = config.BASE_URL + config.STORAGE_PORT + '/api/ibm/object/' + file_name + '/' + file_extension
    response = requests.get(url)
    if response.status_code == 200:
        image_data = BytesIO(response.content)
        return image_data


def put_ibm_object(file_content: bytes, file_extension: str):
    url = config.BASE_URL + config.STORAGE_PORT + '/api/ibm/object'
    files = {'file_content': ('filename', file_content, 'application/octet-stream')}
    params = {'file_extension': file_extension}
    response = requests.put(url, files=files, params=params)
    if response.status_code == 200:
        print("파일 업로드 성공")
    else:
        print(f"파일 업로드 실패: {response.status_code}")

    return response.json()['file_name']
