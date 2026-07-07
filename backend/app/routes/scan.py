from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/scan")
def scan_project():

    files = []

    project_files = {}

    for root, dirs, filenames in os.walk("extracted"):
        print(root)

        for file in filenames:
            files.append(os.path.join(root, file))
            try:
                with open(os.path.join(root, file), "r") as f:
                  content = f.read()
                project_files[file] = content
            except:
                pass

    return {
    "files": files,
    "project_files": project_files
}