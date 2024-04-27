from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from app.commons.constants.constants import Constants
from app.commons.pasword_enconder.crypt import Crypt
from app.commons.pasword_enconder.password_encoder import PasswordEncoder
from app.commons.responses.common_response_DTO import CommonResponseDTO
from app.controllers.user_controller import UserController
from app.dependecies import get_db, get_current_user_active
from app.models.unauthorized import Unauthorized
from app.models.user import User, UserDTO
from app.services.services_impl.user_service_impl import UserServiceImpl
from app.services.user_service import UserService

TAGS = ['Users']
PREFIX = '/users'

router = APIRouter(
    tags=TAGS,
    prefix=PREFIX,
    responses={HTTPStatus.UNAUTHORIZED: {"model": Unauthorized}},
    # dependencies=[Depends(get_current_user_active)]
)
crypt: PasswordEncoder = Crypt()
userService: UserService = UserServiceImpl(crypt)
controller = UserController(userService)


@router.get("/", responses={
    HTTPStatus.OK: {"model": CommonResponseDTO[list[User]]},
    HTTPStatus.BAD_REQUEST: {"model": CommonResponseDTO[str]},
})
async def find_all(response: Response, db: Session = Depends(get_db)):
    users = controller.find_all(db)
    response.status_code = int(users.metadata.statusCode)
    return users


@router.post("/", responses={
    HTTPStatus.OK: {"model": CommonResponseDTO[list[User]]},
    HTTPStatus.BAD_REQUEST: {"model": CommonResponseDTO[str]},
})
async def find_all(user: UserDTO, response: Response, db: Session = Depends(get_db)):
    user = controller.save(user, db)
    response.status_code = int(user.metadata.statusCode)
    return user


@router.delete("/{id_users}", responses={
    HTTPStatus.OK: {"model": CommonResponseDTO[list[User]]},
    HTTPStatus.NOT_FOUND: {"model": CommonResponseDTO[None]},
    HTTPStatus.BAD_REQUEST: {"model": CommonResponseDTO[str]},
})
async def delete(id_user: int, response: Response, db: Session = Depends(get_db)):
    user = controller.delete_by_id(id_user, db)
    response.status_code = int(user.metadata.statusCode)
    return user


@router.get("/profile", responses={
    HTTPStatus.OK: {"model": CommonResponseDTO[User]},
})
async def profile(current_user: Annotated[User, Depends(get_current_user_active)]):
    return CommonResponseDTO.build_response(str(HTTPStatus.OK), Constants.MSG_OK, current_user.model_dump())
