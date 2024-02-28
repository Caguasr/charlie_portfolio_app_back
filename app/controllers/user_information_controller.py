from http import HTTPStatus

from sqlalchemy.orm import Session

from app.commons.constants.constants import Constants
from app.commons.exceptions.common_exception import CommonException
from app.commons.responses.common_response_DTO import CommonResponseDTO
from app.models.user import User
from app.models.user_information import UserInformationDTO
from app.services.user_information_service import UserInformationService


class UserInformationController:

    def __init__(self, user_information_service: UserInformationService):
        self.service = user_information_service

    def get_user_information(self, user: User, db: Session) -> CommonResponseDTO:
        return self.service.get_user_information(user, db)

    def save_user_information(self, user_information: UserInformationDTO, current_user: User,
                              db: Session) -> CommonResponseDTO:
        return self.service.save_user_information(user_information, current_user, db)

    def delete_user_information(self, id_user_information: int,
                                user: User,
                                db: Session) -> CommonResponseDTO:
        return self.service.delete_user_information(id_user_information, user, db)
