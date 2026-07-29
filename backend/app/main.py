from fastapi import FastAPI

from app.api.root import router as root_router
from app.api.health import router as health_router

from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description,
)

app.include_router(root_router)
app.include_router(health_router)