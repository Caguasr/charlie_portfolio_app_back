from http import HTTPStatus

from sqlalchemy.orm import Session

from app.commons.responses.common_response_DTO import CommonResponseDTO
from app.models.auth import AuthDTO
from app.services.JWTService import JWTService
from app.services.auth_service import AuthService


class AuthController:
    def __init__(self, auth_service: AuthService):
        self.auth_service = auth_service

    def login(self, auth_dto: AuthDTO, db: Session):
        try:
            return self.auth_service.login(auth_dto, db)
        except Exception as e:
            return CommonResponseDTO.create_error_response(str(HTTPStatus.INTERNAL_SERVER_ERROR), str(e))
