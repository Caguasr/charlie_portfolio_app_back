from http import HTTPStatus

from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from app.commons.responses.common_response_DTO import CommonResponseDTO
from app.controllers.role_controller import RoleController
from app.dependecies import get_db, oauth2_scheme
from app.models.role import Role, RoleDTO
from app.models.unauthorized import Unauthorized
from app.services.services_impl.role_service_impl import RoleServiceImpl

ENDPOINT_NAME = "/roles"
TAGS = ["Role"]

router = APIRouter(prefix=ENDPOINT_NAME, tags=TAGS, responses={HTTPStatus.UNAUTHORIZED: {"model": Unauthorized}})
controller = RoleController(RoleServiceImpl())


@router.post("/", responses={
    HTTPStatus.OK: {"model": CommonResponseDTO[Role]},
    HTTPStatus.BAD_REQUEST: {"model": CommonResponseDTO[str]}
})
def save(role: RoleDTO, response: Response, db: Session = Depends(get_db)):
    response_controller = controller.save(role, db)
    response.status_code = int(response_controller.metadata.statusCode)
    return response_controller
