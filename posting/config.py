from starlette.config import Config

config = Config('.env')

BASE_URL = config('BASE_URL')

GPT_PORT = config('GPT_PORT')
POSTING_PORT = config('POSTING_PORT')
STORAGE_PORT = config('STORAGE_PORT')

KOGPT_API = config('KOGPT_API')
CHATGPT_API = config('CHATGPT_API')
