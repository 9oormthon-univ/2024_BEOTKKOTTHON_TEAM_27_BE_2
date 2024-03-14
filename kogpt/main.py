from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import kogpt_router

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

app.include_router(kogpt_router.router)


@app.get("/hello")
def hello():
    return {"message": "안녕하세요"}
