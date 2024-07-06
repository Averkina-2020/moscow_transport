from fastapi import APIRouter, HTTPException

from moscow_transport.modules.metro import database, schema

metro_router = APIRouter()


@metro_router.get(
    '/news', name='Новости метро', response_model=list[schema.NewsResponse]
)
async def get_metro_news(days: int):
    news = database.get_news_for_last_n_days(days)
    if not news:
        raise HTTPException(status_code=404, detail='No news found')
    return news
