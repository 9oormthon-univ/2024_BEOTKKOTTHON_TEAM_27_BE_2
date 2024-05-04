import requests
import config
import uuid
from datetime import datetime, timedelta
from fastapi import HTTPException

IBM_CLOUD_URL = 'https://s3.us-south.cloud-object-storage.appdomain.cloud'
IBM_TOKEN_URL = 'https://iam.cloud.ibm.com/identity/token'
BUCKET_NAME = 'image-with-copywriter'

IBM_TOKEN = 'null'
IBM_TOKEN_CREATED_TIME = datetime.utcnow() - timedelta(hours=2)


def get_ibm_token(api_key):
    global IBM_TOKEN, IBM_TOKEN_CREATED_TIME

    if IBM_TOKEN == 'null' or IBM_TOKEN_CREATED_TIME + timedelta(minutes=59) < datetime.utcnow():
        url = IBM_TOKEN_URL
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'grant_type': 'urn:ibm:params:oauth:grant-type:apikey',
            'apikey': api_key
        }

        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            update_ibm_token(response.json()['access_token'])
            print("토큰을 성공적으로 받았습니다")
        else:
            print("토큰 요청 실패:", response.status_code)

    return IBM_TOKEN


def update_ibm_token(ibm_token: str):
    global IBM_TOKEN, IBM_TOKEN_CREATED_TIME
    IBM_TOKEN = ibm_token
    IBM_TOKEN_CREATED_TIME = datetime.utcnow()


def get_file_content(file_name):
    url = IBM_CLOUD_URL + '/' + BUCKET_NAME + '/' + file_name
    headers = {
        'Authorization': 'Bearer ' + get_ibm_token(config.IBM_API_KEY),
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        raise ValueError("Failed to fetch image from URL.")


def get_content_type(file_extension: str):
    if file_extension == '.jpeg' or file_extension == '.jpg':
        return 'image/jpeg'
    elif file_extension == '.png':
        return 'image/png'
    elif file_extension == '.heic':
        return 'image/heic'
    else:
        raise HTTPException(status_code=400, detail="지원하지 않는 파일 형식입니다.")


def upload_file_to_ibm(file_content: bytes, file_extension: str):
    file_name = str(uuid.uuid4()) + file_extension
    url = IBM_CLOUD_URL + '/' + BUCKET_NAME + '/' + file_name
    headers = {
        'Authorization': 'Bearer ' + get_ibm_token(config.IBM_API_KEY),
        'Content-Type': get_content_type(file_extension)
    }

    try:
        response = requests.put(url, data=file_content, headers=headers)
        if response.status_code == 200:
            print("파일 업로드 성공")
        else:
            print(f"파일 업로드 실패: {response.status_code}")

        return file_name
    except Exception as e:
        print(f"오류 발생: {e}")