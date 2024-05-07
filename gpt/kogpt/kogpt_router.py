from fastapi import APIRouter, HTTPException
import requests
import json
import os

from kogpt.kogpt_schema import KoGPTRequest

REST_API_KEY = os.environ.get('REST_API_KEY')
MAX_TOKENS = int(os.environ.get('MAX_TOKENS'))
TEMPERATURE = float(os.environ.get('TEMPERATURE'))
TOP_P = float(os.environ.get('TOP_P'))
N = int(os.environ.get('N'))

router = APIRouter(
    prefix="/api/gpt/kogpt",
)

@router.post("")
def get_result(request: KoGPTRequest):
    r = requests.post(
        'https://api.kakaobrain.com/v1/inference/kogpt/generation',
        json={
            'prompt': request.content,
            'max_tokens': MAX_TOKENS,
            'temperature': TEMPERATURE,
            'top_p': TOP_P,
            'n': N
        },
        headers={
            'Authorization': 'KakaoAK ' + REST_API_KEY,
            'Content-Type': 'application/json'
        }
    )

    response = json.loads(r.content)
    '''
        response = {
            "id": str, # 개별 처리 작업 식별자
            "generations": Generation[], # KoGPT가 생성한 결과 정보 배열
            "usage": Usage # 토큰 사용량
        }
        
        Generation = {
            "text": str, # KoGPT가 생성한 결과
            "tokens": Integer # 결과 토큰 수
        }
        
        Usage = {
            "prompt_tokens": int, # KoGPT에게 전달된 프롬프터의 토큰 수
            "generated_tokens": int, # KoGPT가 생성한 결과의 토큰 수
            "total_tokens": int # 총 토큰 수
        }
    '''

    # print(response["id"])
    # print(response["generations"][0]["text"])

    if r.status_code == 200:
        return {
            "text": response["generations"][0]["text"]
        }
    else:
        raise HTTPException(status_code=400, detail="KoGPT 서버로부터 올바른 응답을 받지 못했습니다")
