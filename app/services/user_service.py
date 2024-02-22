from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.commons.responses.common_response_DTO import CommonResponseDTO
from app.models.user import User, UserDTO


class UserService(ABC):

    @abstractmethod
    def find_all(self, db: Session) -> CommonResponseDTO:
        pass

    @abstractmethod
    def save(self, user: UserDTO, db: Session):
        pass

    @abstractmethod
    def get_user_by_id(self, id_user: int, db: Session) -> CommonResponseDTO:
        pass

    @abstractmethod
    def update(self, id_user: int, user: User, db: Session) -> CommonResponseDTO:
        pass

    @abstractmethod
    def delete(self, id_user: int, db: Session) -> CommonResponseDTO:
        pass
