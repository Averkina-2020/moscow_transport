import logging

from apscheduler.schedulers.blocking import BlockingScheduler

from moscow_transport.modules.metro.database import (SessionLocal,
                                                     add_news_to_db)
from moscow_transport.modules.metro.services import parse_mosday

logging.basicConfig(level=logging.INFO)


def update_news_database():
    logging.info("Start of database update")
    try:
        with SessionLocal() as db:
            news_data = parse_mosday()
            add_news_to_db(db, news_data)
    except Exception as e:
        logging.error(f"Error updating the database: {e}")
    else:
        logging.info("The database has been successfully updated")


scheduler = BlockingScheduler()
scheduler.add_job(update_news_database, 'interval', minutes=3)
try:
    logging.info("Запуск планировщика...")
    scheduler.start()
except KeyboardInterrupt:
    logging.info("Планировщик остановлен.")
