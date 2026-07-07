from fastapi import APIRouter

router = APIRouter()

@router.get("/features")
def features():
    return {
        "features": [
            "API Discovery",
            "Documentation",
            "Dependency Analysis",
            "Security Review",
            "Health Score"
        ]
    }