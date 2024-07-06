FROM python:3.9

WORKDIR /app

# Установка необходимых пакетов для подключения к PostgreSQL
RUN apt-get update && \
    apt-get install -y wget postgresql-client && \
    mkdir -p ~/.postgresql && \
    wget "https://storage.yandexcloud.net/cloud-certs/CA.pem" \
         -O ~/.postgresql/root.crt && \
    chmod 0600 ~/.postgresql/root.crt

COPY ./Moscow_trannsport/poetry.lock ./Moscow_trannsport/pyproject.toml ./
RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-root

COPY ./Moscow_trannsport/ .

# Настройка переменных окружения для подключения к БД

ENV POSTGRES_HOST
ENV POSTGRES_PORT
ENV POSTGRES_USER
ENV POSTGRES_PASSWORD
ENV POSTGRES_DB

# Запуск парсера

CMD ["python", "-m", "moscow_transport.modules.metro.scheduler"]
