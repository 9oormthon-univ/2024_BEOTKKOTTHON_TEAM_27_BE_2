from starlette.config import Config

config = Config('.env')

BASE_URL = config('BASE_URL')
KOGPT_API = config('KOGPT_API')
CHATGPT_API = config('CHATGPT_API')
