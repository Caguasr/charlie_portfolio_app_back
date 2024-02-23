from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.models.user import User


class TokenKeyService(ABC):

    @abstractmethod
    def create_token_key(self, user: User, db: Session):
        pass

    @abstractmethod
    def get_token_key(self, current_user: User, db: Session):
        pass
