from http import HTTPStatus

from sqlalchemy.orm import Session

from app.commons.constants.constants import Constants
from app.commons.pasword_enconder.password_encoder import PasswordEncoder
from app.commons.responses.common_response_DTO import CommonResponseDTO
from app.entities.user import User as UserEntity
from app.models.user import User, UserDTO
from app.services.user_service import UserService


class UserServiceImpl(UserService):

    def __init__(self, crypt_password: PasswordEncoder):
        self.crypt_password = crypt_password

    def find_all(self, db: Session) -> CommonResponseDTO:
        try:
            users = db.query(UserEntity).all()
            to_json = [User(**user.to_dict()).model_dump() for user in users]
            return CommonResponseDTO.build_response(str(HTTPStatus.OK), Constants.MSG_OK, to_json)
        except Exception as e:
            return CommonResponseDTO.build_response(str(HTTPStatus.BAD_REQUEST), Constants.MSG_ERROR, str(e))

    def save(self, user: UserDTO, db: Session):
        try:
            new_user = UserEntity(**user.__dict__)
            new_user.active = True
            hashed_password = self.crypt_password.hash(user.password)
            new_user.password = hashed_password
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            to_json = User(**new_user.to_dict()).model_dump()
            return CommonResponseDTO.build_response(str(HTTPStatus.OK), Constants.MSG_OK, to_json)
        except Exception as e:
            db.rollback()
            return CommonResponseDTO.build_response(str(HTTPStatus.BAD_REQUEST), Constants.MSG_ERROR, str(e))

    def get_user_by_id(self, id_user: int, db: Session) -> CommonResponseDTO:
        try:
            user = db.query(UserEntity).filter(UserEntity.id == id_user).first()
            if user is None:
                return CommonResponseDTO.build_response(str(HTTPStatus.NOT_FOUND), Constants.MSG_NOT_FOUND, None)
            to_json = User(**user.to_dict()).model_dump()
            return CommonResponseDTO.build_response(str(HTTPStatus.OK), Constants.MSG_OK, to_json)
        except Exception as e:
            return CommonResponseDTO.build_response(str(HTTPStatus.BAD_REQUEST), Constants.MSG_ERROR, str(e))

    def update(self, id_user: int, user: User, db: Session) -> CommonResponseDTO:
        pass

    def delete(self, id_user: int, db: Session) -> CommonResponseDTO:
        try:
            user = db.query(UserEntity).filter(UserEntity.id == id_user).first()
            if user is None:
                return CommonResponseDTO.build_response(str(HTTPStatus.NOT_FOUND), Constants.MSG_NOT_FOUND, None)
            db.delete(user)
            db.commit()
            return CommonResponseDTO.build_response(str(HTTPStatus.OK), Constants.MSG_OK, None)
        except Exception as e:
            return CommonResponseDTO.build_response(str(HTTPStatus.BAD_REQUEST), Constants.MSG_ERROR, str(e))
