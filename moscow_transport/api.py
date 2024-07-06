from fastapi import APIRouter

from .modules.metro.endpoints import metro_router

api_router = APIRouter()

api_router.include_router(metro_router, prefix='/metro', tags=['Метро'])
