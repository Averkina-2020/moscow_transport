from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    main_url: str


settings = Settings()
