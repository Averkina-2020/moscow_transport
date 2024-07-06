from datetime import date

from pydantic import BaseModel, Field


class NewsResponse(BaseModel):
    title: str = Field(..., title='Заголовок')
    publication_text: str = Field(None, title='Текст новости')
    image_url: str = Field(None, title='URL изображения')
    pubdate: date = Field(None, title='Дата публикации')
