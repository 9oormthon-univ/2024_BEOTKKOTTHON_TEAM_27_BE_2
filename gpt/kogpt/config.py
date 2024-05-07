import os

# KoGPT
REST_API_KEY = os.environ.get('REST_API_KEY')
MAX_TOKENS = int(os.environ.get('MAX_TOKENS'))
TEMPERATURE = float(os.environ.get('TEMPERATURE'))
TOP_P = float(os.environ.get('TOP_P'))
N = int(os.environ.get('N'))
