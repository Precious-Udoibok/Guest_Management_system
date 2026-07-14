from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.api_v1.api import api_router


app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API endpoints for Guest Management System, "
    "a Visitor Management System built with FastAPI ",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "GMS API Homepage"}


app.include_router(api_router, prefix=settings.API_V1_STR)
