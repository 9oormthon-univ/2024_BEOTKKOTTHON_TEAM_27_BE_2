from PIL import Image
from io import BytesIO
import requests

from generating.posting_schema import PostingTextRequest, PostingImageRequest
from editing.edit_image import put_text_on_image

BASEURL = 'http://localhost:'
STORAGE_PORT = '8082'

def create_prompt_text(request: PostingTextRequest):
    prompt_message = f"정보: 나는 <{request.store.name}>를 운영하고 있는 사장이야. \
                    {request.store.address}에 위치하고 있어. \
                    {request.promotion.subject}라는 신메뉴가 출시되었어. \
                    {request.promotion.channel} 홍보 글을 올리고 싶어. \
                    {request.promotion.target}를 타깃으로 하고 있어. \
                    '{request.promotion.content}'를 강조해서 홍보하고 싶어. \
                    예시: 안녕하세요! 용인시 기흥구에 위치한 <맛있는 버블티 가게>입니다. 이번에 새롭게 출시된 얼그레이 밀크티로 여러분을 초대합니다. 우리의 특별한 밀크폼이 올라간 이 티는 입안을 감미롭게 만들어줄 것입니다. 산뜻한 얼그레이 향과 부드러운 우유의 조화는 당신의 입맛을 만족시킬 것입니다. 이제 당신도 새로운 맛의 세계로 여행을 떠나보세요. 얼그레이 밀크티와 함께 매혹적인 맛을 경험해보세요! \
                    요청: 정보와 예시를 바탕으로 광고 글을 1개 작성해줘! 300자를 넘기지마. 그리고, 공손한 말투로 만들어줘.\
                    광고 글:"
    return prompt_message


def create_prompt_image(request: PostingImageRequest):
    prompt_message = f"정보: 나는 <{request.store.name}>를 운영하고 있는 사장이야. \
                        {request.store.address}에 위치하고 있어. \
                        {request.promotion.subject}라는 신메뉴가 출시되었어. \
                        {request.promotion.channel} 홍보 글을 올리고 싶어. \
                        '{request.promotion.content}'를 강조해서 홍보하고 싶어. \
                        예시: 숙대 앞 매운 닭발의 환상! 20대 남성의 입맛을 사로잡는 최고 맛집! #엽기떡볶이 #매운닭발 #숙명여대 \
                        요청: 정보와 예시를 바탕으 카피라이터을 1개 작성해줘! 40자를 넘기지마. 짧은 글이야. 명심해. \
                        카피라이터:"
    return prompt_message


def create_image(file_name: str, text: str):
    image_data = get_ibm_object(file_name)

    image = Image.open(image_data)
    new_image = put_text_on_image(image, text, "../font/MaruBuri-Bold.ttf", 150, "black")

    buffer = BytesIO()
    new_image.save(buffer, format="JPEG")
    new_file_name = put_ibm_object(buffer.getvalue(), '.jpeg')
    return new_file_name


def get_ibm_object(file_name: str, file_extension: str):
    url = BASEURL + STORAGE_PORT + '/api/storage/ibm/object/' + file_name + '/' + file_extension
    response = requests.get(url)
    if response.status_code == 200:
        image_data = BytesIO(response.content)
        return image_data


def put_ibm_object(file_content: bytes, file_extension: str):
    url = BASEURL + STORAGE_PORT + '/api/storage/ibm/object'
    files = {'file_content': ('filename', file_content, 'application/octet-stream')}
    params = {'file_extension': file_extension}
    response = requests.put(url, files=files, params=params)
    if response.status_code == 200:
        print("파일 업로드 성공")
    else:
        print(f"파일 업로드 실패: {response.status_code}")

    return response.json()['file_name']
