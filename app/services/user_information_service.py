from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.commons.responses.common_response_DTO import CommonResponseDTO
from app.models.user_information import UserInformationDTO


class UserInformationService(ABC):

    @abstractmethod
    def get_user_information(self, db: Session) -> CommonResponseDTO:
        pass

    @abstractmethod
    def save_user_information(self, user_information: UserInformationDTO, db: Session) -> CommonResponseDTO:
        pass

    @abstractmethod
    def delete_user_information(self, id: int, db: Session) -> CommonResponseDTO:
        pass
