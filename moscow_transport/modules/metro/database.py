import os
from datetime import date, timedelta

from dotenv import load_dotenv
from sqlalchemy import MetaData, Table, create_engine, insert, select
from sqlalchemy.orm import sessionmaker

from moscow_transport.modules.metro.schema import NewsResponse

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={'sslmode': 'verify-full'},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadata = MetaData()
metadata.reflect(bind=engine)
metro_news = Table('metro_news', metadata)


def get_news_for_last_n_days(days: int):
    db = SessionLocal()
    today = date.today()
    first_search_day = today - timedelta(days=days)
    db_query = select(metro_news).where(metro_news.c.pubdate >= first_search_day)
    result = db.execute(db_query).fetchall()
    db.close()

    news_list = [
        NewsResponse(
            title=row.title,
            publication_text=row.pub_text,
            image_url=row.image_url,
            pubdate=row.pubdate,
        )
        for row in result
    ]
    return news_list


def is_news_exists(db, title, pubdate):
    query = select(metro_news).where(
        metro_news.c.title == title,
        metro_news.c.pubdate == pubdate
    )
    result = db.execute(query).fetchone()
    return bool(result)


def add_news_to_db(db, news_data):
    for news in news_data:
        if not is_news_exists(db, news['title'], news['pubdate']):
            query = insert(metro_news).values(**news)
            db.execute(query)
    db.commit()
