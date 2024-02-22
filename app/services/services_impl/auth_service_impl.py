from datetime import timedelta
from http import HTTPStatus

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.commons.constants.constants import Constants
from app.commons.pasword_enconder.password_encoder import PasswordEncoder
from app.commons.responses.common_response_DTO import CommonResponseDTO
from app.configs.environment import environment
from app.entities.user import User as UserEntity
from app.models.auth import AuthDTO
from app.models.user import User
from app.services.JWTService import JWTService
from app.services.auth_service import AuthService

EXPIRES_JWT = environment.time_expires_token


class AuthServiceImpl(AuthService):

    def __init__(self, crypt_password: PasswordEncoder, jwt_service: JWTService):
        self.crypt_password = crypt_password
        self.jwt_service = jwt_service

    def login(self, auth: AuthDTO, db: Session):
        try:
            user: UserEntity = db.query(UserEntity).filter(UserEntity.username == auth.username).first()
            if user is None:
                return CommonResponseDTO.build_response(str(HTTPStatus.BAD_REQUEST), Constants.MSG_ERROR,
                                                        Constants.MSG_INVALID_CREDENTIALS)
            is_valid_password = self.crypt_password.verify(auth.password, user.password)
            if is_valid_password is False:
                return CommonResponseDTO.build_response(str(HTTPStatus.BAD_REQUEST), Constants.MSG_ERROR,
                                                        Constants.MSG_INVALID_CREDENTIALS)
            data = {
                "sub": str(user.id)
            }
            jwt = self.jwt_service.create_access_token(data, timedelta(minutes=EXPIRES_JWT))
            return CommonResponseDTO.build_response(str(HTTPStatus.OK), Constants.MSG_OK, jwt)
        except SQLAlchemyError as e:
            return CommonResponseDTO.build_response(str(HTTPStatus.BAD_REQUEST), Constants.MSG_ERROR, str(e))
