from fastapi import APIRouter
import config
import requests

router = APIRouter(
    prefix="/api/storage",
)
