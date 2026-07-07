from fastapi import APIRouter, UploadFile, File
import os
import zipfile

router = APIRouter()

UPLOAD_FOLDER = "uploads"
EXTRACT_FOLDER = "extracted"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(EXTRACT_FOLDER, exist_ok=True)

@router.post("/upload")
async def upload_project(file: UploadFile = File(...)):

    try:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        contents = await file.read()

        with open(file_path, "wb") as f:
            f.write(contents)

        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(EXTRACT_FOLDER)

        return {
            "filename": file.filename,
            "message": "File uploaded & extracted successfully!"
        }

    except Exception as e:
        return {
            "error": str(e)
        }