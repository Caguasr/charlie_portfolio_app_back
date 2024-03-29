from http import HTTPStatus

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.commons.constants.constants import Constants
from app.commons.responses.common_response_DTO import CommonResponseDTO
from app.models.user_information import UserInformation, UserInformationDTO
from app.services.user_information_service import UserInformationService


class UserInformationController:

    def __init__(self, user_information_service: UserInformationService):
        self.service = user_information_service

    def get_user_information(self, db: Session) -> CommonResponseDTO:
        try:
            return self.service.get_user_information(db)
        except Exception as e:
            return CommonResponseDTO.build_response(str(HTTPStatus.BAD_REQUEST), Constants.MSG_ERROR, str(e))

    def save_user_information(self, user_information: UserInformationDTO, db: Session) -> CommonResponseDTO:
        return self.service.save_user_information(user_information, db)

    def delete_user_information(self, id_user_information: int, db: Session) -> CommonResponseDTO:
        return self.service.delete_user_information(id_user_information, db)
