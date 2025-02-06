from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routes import router
from app.config import settings

app = FastAPI(title="Milo API", description="AI service to answer Religion related question with the science aspect")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors.allow_origins,
    allow_methods=settings.cors.allow_methods,
    allow_headers=settings.cors.allow_headers,
    allow_credentials=settings.cors.allow_credentials,
)

app.include_router(router)
