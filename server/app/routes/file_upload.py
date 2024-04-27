from fastapi import APIRouter, File, UploadFile, HTTPException
from typing import List
from app.services.file_upload_service import create_folder_upload_files
from app.constant import FILE_UPLOAD_LIMIT

router = APIRouter()


@router.post("/upload-files/")
async def upload_files(
    files: List[UploadFile] = File(..., description="Files to be uploaded")
):
    if len(files) > FILE_UPLOAD_LIMIT:
        raise HTTPException(
            status_code=400, detail="You can upload up to 3 files at a time."
        )

    # call service to upload files
    temp_folder = await create_folder_upload_files(files)

    # Return the temporary folder path
    return {"temp_folder": temp_folder}
