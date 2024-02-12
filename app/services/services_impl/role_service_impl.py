from http import HTTPStatus

from sqlalchemy.orm import Session

from app.commons.constants.constants import Constants
from app.commons.responses.common_response_DTO import CommonResponseDTO
from app.entities.role import Role as RoleEntity
from app.models.role import RoleDTO, Role
from app.services.role_service import RoleService


class RoleServiceImpl(RoleService):

    def save(self, role: RoleDTO, db: Session) -> CommonResponseDTO:
        try:
            role = RoleEntity(**role.model_dump())
            db.add(role)
            db.commit()
            db.refresh(role)
            to_model = Role(**role.__dict__)
            return CommonResponseDTO.build_response(str(HTTPStatus.OK), Constants.MSG_OK, to_model.model_dump())
        except Exception as e:
            return CommonResponseDTO.build_response(str(HTTPStatus.BAD_REQUEST), Constants.MSG_ERROR, str(e))
