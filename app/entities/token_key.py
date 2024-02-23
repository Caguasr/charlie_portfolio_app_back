from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from app.configs.database import Base


class TokenKey(Base):
    __tablename__ = 'token_keys'
    id: int = Column(Integer, primary_key=True)
    token: str = Column(String, unique=True)
    user_id: int = Column(Integer, ForeignKey('users.id'))
    created_at: datetime = Column(DateTime, default=datetime.now())
