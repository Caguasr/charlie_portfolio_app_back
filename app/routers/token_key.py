from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from app.commons.responses.common_response_DTO import CommonResponseDTO
from app.controllers.token_key_controller import TokenKeyController
from app.dependecies import get_current_user_active, get_db
from app.models.user import User
from app.services.services_impl.token_key_service_impl import TokenKeyServiceImpl

TAGS = ["API Token Key"]
PREFIX = "/token-key"

router = APIRouter(
    tags=TAGS,
    prefix=PREFIX
)

_service = TokenKeyServiceImpl()
_controller = TokenKeyController(_service)


@router.get("", responses={
    HTTPStatus.OK: {"description": "Api key token", "model": CommonResponseDTO[str]},
    HTTPStatus.NOT_FOUND: {"description": "No api key found", "model": CommonResponseDTO[None]}
})
async def get_token_key(response: Response, user: Annotated[User, Depends(get_current_user_active)],
                        db: Session = Depends(get_db)):
    response_controller = _controller.get_token_key_by_user_id(user, db)
    response.status_code = int(response_controller.metadata.statusCode)
    return response_controller


@router.post("", responses={
    HTTPStatus.OK: {"description": "Api key token", "model": CommonResponseDTO[None]},
})
async def save_new_token(response: Response, user: Annotated[User, Depends(get_current_user_active)],
                         db: Session = Depends(get_db)):
    response_controller = _controller.save_token_key(user, db)
    response.status_code = int(response_controller.metadata.statusCode)
    return response_controller
