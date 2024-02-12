from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.configs.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    active = Column(Boolean)
    created_at = Column(DateTime, default=datetime.now())
    role_id = Column(Integer, ForeignKey('roles.id'))

    role = relationship("Role", back_populates="user")
    information = relationship("UserInformation", back_populates="user")
