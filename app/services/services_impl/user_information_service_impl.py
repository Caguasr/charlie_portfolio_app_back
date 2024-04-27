from http import HTTPStatus

from sqlalchemy import asc, desc, and_
from sqlalchemy.orm import Session

from app.commons.constants.constants import Constants
from app.commons.responses.common_response_DTO import CommonResponseDTO
from app.entities.user_information import UserInformation as UserInformationEntity
from app.models.user import User
from app.models.user_information import UserInformationDTO, UserInformation
from app.services.user_information_service import UserInformationService


class UserInformationServiceImpl(UserInformationService):

    def get_user_information(self, user: User, db: Session) -> CommonResponseDTO:
        try:
            user_information = (db.query(UserInformationEntity)
                                .filter(UserInformationEntity.user_id == user.id)
                                .order_by(desc(UserInformationEntity.active))
                                .all()
                                )
            list_user_information = map(lambda item: UserInformation(**item.__dict__).model_dump(), user_information)
            return (CommonResponseDTO[UserInformation]
                    .build_response(str(HTTPStatus.OK), Constants.MSG_OK, list_user_information))
        except Exception as e:
            return CommonResponseDTO.build_response(str(HTTPStatus.BAD_REQUEST), Constants.MSG_ERROR, e)

    def save_user_information(self, user_information: UserInformationDTO, user: User, db: Session):
        try:
            self._update_active_user_information(False, user, db)
            new_user = UserInformationEntity(**user_information.model_dump())
            new_user.user_id = user.id
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            to_model = UserInformation(**new_user.__dict__)
            return CommonResponseDTO[UserInformation].build_response(str(HTTPStatus.CREATED), Constants.MSG_OK,
                                                                     to_model)
        except Exception as e:
            return CommonResponseDTO.build_response(str(HTTPStatus.BAD_REQUEST), Constants.MSG_ERROR, str(e))

    def delete_user_information(self, id_user_information: int, user: User, db: Session) -> CommonResponseDTO:
        try:
            user = (db.query(UserInformationEntity).filter(
                and_(UserInformationEntity.id == id_user_information, UserInformationEntity.user_id == user.id))
                    .first())
            if user is None:
                return (CommonResponseDTO
                        .build_response(str(HTTPStatus.NOT_FOUND), Constants.MSG_ERROR, Constants.MSG_NOT_FOUND))
            db.delete(user)
            db.commit()
            return CommonResponseDTO.build_response(str(HTTPStatus.OK), Constants.MSG_OK, None)
        except Exception as e:
            return CommonResponseDTO.build_response(str(HTTPStatus.BAD_REQUEST), Constants.MSG_ERROR, str(e))

    @staticmethod
    def _update_active_user_information(status: bool, user: User, db: Session):
        try:
            db.query(UserInformationEntity).filter(and_(
                UserInformationEntity.active == True, UserInformationEntity.user_id == user.id)).update(
                {"active": status})
            db.commit()
        except Exception as e:
            return CommonResponseDTO.build_response(str(HTTPStatus.BAD_REQUEST), Constants.MSG_ERROR, str(e))
