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

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'active': self.active,
            'created_at': self.created_at if self.created_at else None,
            'role_id': self.role_id,
            'role': self.role.__dict__ if self.role else None,
        }
