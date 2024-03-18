from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from generating import posting_router

app = FastAPI()

origins = [
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posting_router.router)