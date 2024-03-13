from starlette.config import Config

config = Config('.env')
REST_API_KEY = config('REST_API_KEY')