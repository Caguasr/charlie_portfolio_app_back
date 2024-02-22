from http import HTTPStatus

from sqlalchemy.orm import Session

from app.commons.constants.constants import Constants
from app.commons.responses.common_response_DTO import CommonResponseDTO
from app.entities.role import Role as RoleEntity
from app.models.role import RoleDTO, Role
from app.services.role_service import RoleService


class RoleServiceImpl(RoleService):

    def find_all(self, db: Session) -> CommonResponseDTO:
        try:
            roles = db.query(RoleEntity).all()
            roles_to_json = []
            for role in roles:
                roles_to_json.append(Role(**role.__dict__).model_dump())
            return CommonResponseDTO.build_response(str(HTTPStatus.OK), Constants.MSG_OK, roles_to_json)
        except Exception as ex:
            return CommonResponseDTO.build_response(str(HTTPStatus.BAD_REQUEST), Constants.MSG_ERROR, str(ex))

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

    def delete(self, id_role: int, db: Session) -> CommonResponseDTO:
        try:
            role = db.query(RoleEntity).filter(RoleEntity.id == id_role).first()
            if role is None:
                return CommonResponseDTO.build_response(str(HTTPStatus.NOT_FOUND), Constants.MSG_NOT_FOUND, None)
            db.delete(role)
            db.commit()
            return CommonResponseDTO.build_response(str(HTTPStatus.OK), Constants.MSG_OK, None)
        except Exception as ex:
            return CommonResponseDTO.build_response(str(HTTPStatus.BAD_REQUEST), Constants.MSG_ERROR, str(ex))
