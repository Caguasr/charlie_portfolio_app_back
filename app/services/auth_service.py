from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.models.auth import AuthDTO


class AuthService(ABC):
    @abstractmethod
    def login(self, auth: AuthDTO, db: Session):
        pass
