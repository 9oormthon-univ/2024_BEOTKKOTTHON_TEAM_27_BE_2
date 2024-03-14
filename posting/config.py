from starlette.config import Config

config = Config('.env')

BASE_URL = config('BASE_URL')