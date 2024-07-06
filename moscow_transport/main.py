from fastapi import FastAPI

from .api import api_router

app = FastAPI(
    title='Безопасный транспорт - API'
)
app.include_router(api_router)
