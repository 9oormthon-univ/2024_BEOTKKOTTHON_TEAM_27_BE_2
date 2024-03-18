from starlette.config import Config

config = Config('.env')

IBM_API_KEY = config('IBM_API_KEY')
