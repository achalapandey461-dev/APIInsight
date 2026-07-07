from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return {
        "project": "APIInsight",
        "developer": "Sunil",
        "version": "1.0"
    }