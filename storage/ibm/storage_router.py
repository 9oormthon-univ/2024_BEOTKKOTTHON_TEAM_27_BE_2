from fastapi import APIRouter, Response, UploadFile

from ibm.storage_crud import *

router = APIRouter(
    prefix="/api/storage/ibm",
)


@router.get("/token")
def get_token():
    ibm_token = get_ibm_token(config.IBM_API_KEY)
    return {
        "ibm_token": ibm_token
    }


@router.get("/object")
def get_ibm_object(file_name: str):
    file: bytes | None = get_file_content(file_name)
    return Response(content=file, media_type="application/octet-stream", headers={"Content-Disposition": f"attachment; filename={file_name}"})



@router.put("/object")
def put_ibm_object(file_content: UploadFile, file_extension: str):
    file_name = upload_file_to_ibm(file_content.file.read(), file_extension)
    return {
        "file_name": file_name
    }