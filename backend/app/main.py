from fastapi import FastAPI

from app.api.root import router as root_router
from app.api.health import router as health_router

app = FastAPI(
    title="AI Chatbot API",
    version="1.0.0",
    description="Backend API for the AI Chatbot project.",
)

app.include_router(root_router)
app.include_router(health_router)