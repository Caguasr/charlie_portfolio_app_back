import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(BaseSettings):
    db_host: str = os.environ.get("DB_HOST")
    db_port: int = os.environ.get("DB_PORT")
    db_username: str = os.environ.get("DB_USERNAME")
    db_password: str = os.environ.get("DB_PASSWORD")
    db_name: str = os.environ.get("DB_NAME")
    secret_key: str = os.environ.get("SECRET_KEY")

    model_config = SettingsConfigDict(env_file=".env")


environment = Environment()
