from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DatabaseConfig:
    def __init__(self, host: str, port: int, username: str, password: str, database: str):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database

    def create_engine(self):
        return create_engine(f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}")

    def create_session(self):
        return sessionmaker(autocommit=False, bind=self.create_engine())


Base = declarative_base()
