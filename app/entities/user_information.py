from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.configs.database import Base


class UserInformation(Base):
    __tablename__ = "users_information"
    id = Column(Integer, primary_key=True, autoincrement=True)
    about = Column(String, nullable=False)
    photo = Column(String, nullable=False)
    position = Column(String, nullable=False)
    active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="information")
