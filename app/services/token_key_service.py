from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.commons.responses.common_response_DTO import CommonResponseDTO
from app.models.user import User


class TokenKeyService(ABC):

    @abstractmethod
    def create_token_key(self, user: User, db: Session):
        pass

    @abstractmethod
    def get_token_key(self, current_user: User, db: Session):
        pass

    @abstractmethod
    def get_token_key_by_value(self, value: str, db: Session) -> CommonResponseDTO:
        pass
