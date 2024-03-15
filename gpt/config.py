from starlette.config import Config

config = Config('.env')

OPENAI_KEY = config('OPENAI_KEY')

REST_API_KEY = config('REST_API_KEY')
MAX_TOKENS = config('MAX_TOKENS')
TEMPERATURE = config('TEMPERATURE')
TOP_P = config('TOP_P')
N = config('N')