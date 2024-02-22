from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Response, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.commons.pasword_enconder.crypt import Crypt
from app.commons.responses.common_response_DTO import CommonResponseDTO
from app.dependecies import get_db
from app.models.auth import AuthDTO, AuthToken
from app.services.services_impl.auth_service_impl import AuthServiceImpl
from app.utils.jwt_util import JWTUtil

TAGS = ["Authentication"]
PREFIX = "/auth"
router = APIRouter(tags=TAGS, prefix=PREFIX)

encrypt_password = Crypt()
jwt = JWTUtil()
auth_service = AuthServiceImpl(encrypt_password, jwt)


@router.post("/login", responses={
    HTTPStatus.OK: {"description": "Access token", "model": AuthToken},
    HTTPStatus.BAD_REQUEST: {"description": "Access token", "model": CommonResponseDTO[str]}
})
async def login(auth_form: Annotated[OAuth2PasswordRequestForm, Depends()], response: Response, db: Session = Depends(get_db)):
    auth_dto = AuthDTO(username=auth_form.username, password=auth_form.password)
    response_controller = auth_service.login(auth_dto, db)
    response.status_code = int(response_controller.metadata.statusCode)
    if response_controller.metadata.statusCode == str(HTTPStatus.OK):
        return AuthToken(access_token=response_controller.data, token_type='bearer').model_dump()
    return response_controller
