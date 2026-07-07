from fastapi import FastAPI

from app.routes.home import router as home_router
from app.routes.about import router as about_router
from app.routes.health import router as health_router
from app.routes.features import router as features_router
from app.routes.upload import router as upload_router
from app.routes.scan import router as scan_router

app = FastAPI(
    title="APIInsight",
    version="1.0.0",
    description="AI-Assisted Discovery, Documentation and Dependency Analysis of Web APIs"
)

app.include_router(home_router)
app.include_router(about_router)
app.include_router(health_router)
app.include_router(features_router)
app.include_router(upload_router)
app.include_router(scan_router)
