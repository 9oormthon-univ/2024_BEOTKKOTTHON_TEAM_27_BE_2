from PIL import Image
from io import BytesIO
import requests
import os

from generating.posting_schema import PostingTextRequest, PostingImageRequest
from editing.edit_image import put_text_on_image

BASE_URL = os.environ.get('BASE_URL')
STORAGE_PORT = os.environ.get('STORAGE_PORT')


font_list = ['WAGURI-TTF.ttf', 'DNFBitBitv2.ttf', 'goryung-strawberry.ttf', 'SDSamliphopangcheTTFOutline.ttf', 'Jalnan2TTF.ttf', 'KakaoBold.ttf']

def create_prompt_text(request: PostingTextRequest):
    prompt_message_primary = '''답변 예시
    가게 이름: 마라탕 숙명여대점
    가게 주소: 서울특별시 용산구
    홍보 주제: 꿔바로우
    홍보 채널: 인스타
    홍보 대상: 20대 남성, 20대 여성
    강조할 내용: 바삭함
    답변:
    🔥🍲 마라탕 숙명여대점, 인스타에서 뜨거운 신제품 소식! 🔥🍲
    서울 용산구의 맛있는 마라탕으로 유명한 저희 가게가 더욱 뜨거워지고 있어요! 이번에는 특별한 메뉴 소식을 전해드리려고 해요. 바로 "꿔바로우"를 소개합니다! 🥟🔥
    마라탕의 진가를 그대로 느낄 수 있는 이 꿔바로우는 바삭한 식감이 일품이에요. 한 입 베어먹으면 바로 입안 가득 퍼지는 고소함과 함께 마라의 진한 맛이 가득 느껴져요. 또한, 특별한 조리법으로 더욱 고소하고 바삭한 맛을 느낄 수 있답니다.
    인스타그램에서만 만나볼 수 있는 단 하나의 맛, 꿔바로우를 맛보시고 싶으신 분들은 지금 저희 마라탕 숙명여대점을 방문해주세요! 여러분의 입맛을 자극할 특별한 맛을 선사할게요. 함께 맛있는 순간을 만들어보세요! 🔥🥢✨
    📍 마라탕 숙명여대점
    📌 서울특별시 용산구
    #마라탕숙명여대점 #꿔바로우 #뜨거운맛 #마라소스 #맛있는마라특제어 #바삭바삭 #매콤달콤 #20대맛집 #인스타푸드'''

    prompt_message = f"정보: 나는 <{request.store.name}>를 운영하고 있는 사장이야. \
                    {request.store.address}에 위치하고 있어. \
                    {request.promotion.subject}라는 신메뉴가 출시되었어. \
                    {request.promotion.channel} 홍보 글을 올리고 싶어. \
                    {request.promotion.targetAge} + {request.promotion.targetGender}를 타깃으로 하고 있어. \
                    '{request.promotion.content}'를 강조해서 홍보하고 싶어. \
                    예시: 안녕하세요! 용인시 기흥구에 위치한 <맛있는 버블티 가게>입니다. 이번에 새롭게 출시된 얼그레이 밀크티로 여러분을 초대합니다. 우리의 특별한 밀크폼이 올라간 이 티는 입안을 감미롭게 만들어줄 것입니다. 산뜻한 얼그레이 향과 부드러운 우유의 조화는 당신의 입맛을 만족시킬 것입니다. 이제 당신도 새로운 맛의 세계로 여행을 떠나보세요. 얼그레이 밀크티와 함께 매혹적인 맛을 경험해보세요! \
                    요청: 정보와 예시를 바탕으로 광고 글을 1개 작성해줘! 600자를 원해. 그리고, 공손한 말투로 만들어줘.\
                    광고 글: "
    return prompt_message_primary + prompt_message

def create_prompt_image(request: PostingImageRequest):
    prompt_message = (f'''가게 이름: {request.store.name} \
                    가게 주소: {request.store.address} \
                    홍보 주제: {request.promotion.subject} \
                    홍보 채널: {request.promotion.channel} \
                    홍보 대상: {request.promotion.targetAge} + {request.promotion.targetGender} \
                    강조할 내용: {request.promotion.content} \
                    
                    이 가게를 홍보할 수 있는 해시태그 3개 만들어줘!! 다 합쳐서 20자를 넘기지마!''')
    return prompt_message


def create_image(file_name: str, subject: str, text: str):
    image_data = get_ibm_object(file_name.split('.')[0], '.' + file_name.split('.')[1])

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
