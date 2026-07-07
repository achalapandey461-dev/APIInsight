from fastapi import APIRouter, UploadFile, File
import os
import zipfile

router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/upload")
async def upload_project(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    contents = await file.read()

    with open(file_path, "wb") as f:
        f.write(contents)

    EXTRACT_FOLDER = "extracted"

    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(EXTRACT_FOLDER)

    return {
        "filename": file.filename,
        "message": "File uploaded successfully!",
        "saved_at": file_path
    }