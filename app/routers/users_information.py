from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, Response, Header
from sqlalchemy.orm import Session

from app.commons.constants.constants import Constants
from app.commons.responses.common_response_DTO import CommonResponseDTO
from app.controllers.user_information_controller import UserInformationController
from app.dependecies import get_db, get_current_user_active, validate_api_key_token
from app.models.unauthorized import Unauthorized
from app.models.user import User
from app.models.user_information import UserInformationDTO, UserInformation
from app.services.services_impl.user_information_service_impl import UserInformationServiceImpl

ENDPOINT_NAME = "/users-information"
TAGS = ["User information"]

router = APIRouter(
    prefix=ENDPOINT_NAME,
    tags=TAGS,
    responses={HTTPStatus.UNAUTHORIZED: {"model": Unauthorized}},
)

controller = UserInformationController(UserInformationServiceImpl())


@router.get("/", responses={str(HTTPStatus.OK): {"model": CommonResponseDTO[list[UserInformation]]}})
def get_user_info(
        current_user: User = Depends(validate_api_key_token),
        db: Session = Depends(get_db)) -> CommonResponseDTO:
    return controller.get_user_information(current_user, db)


@router.post("/", responses={str(HTTPStatus.OK): {"model": CommonResponseDTO[UserInformation]}})
async def save_user_information(user_information: UserInformationDTO,
                                current_user: User = Depends(validate_api_key_token),
                                db: Session = Depends(get_db)) -> CommonResponseDTO:
    return controller.save_user_information(user_information, current_user, db)


@router.delete("/{id_user_information}", responses={
    str(HTTPStatus.OK): {"model": CommonResponseDTO[None]},
    str(HTTPStatus.NOT_FOUND): {"model": CommonResponseDTO[str]}
})
def delete_user_information(id_user_information: int,
                            response: Response,
                            current_user: User = Depends(validate_api_key_token),
                            db: Session = Depends(get_db)):
    delete_response = controller.delete_user_information(id_user_information, current_user, db)
    response.status_code = int(delete_response.metadata.statusCode)
    return delete_response
