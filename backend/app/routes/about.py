from fastapi import APIRouter

router = APIRouter()

@router.get("/about")
def about():
    return {
        "name": "APIInsight",
        "version": "1.0.0",
        "description": "AI-Assisted Discovery, Documentation and Dependency Analysis of Web APIs"
    }