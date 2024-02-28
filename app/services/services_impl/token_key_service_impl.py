import os
from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.commons.constants.constants import Constants
from app.commons.exceptions.common_exception import CommonException
from app.commons.responses.common_response_DTO import CommonResponseDTO
from app.entities.token_key import TokenKey as TokenKeyEntity
from app.models.token_key import TokenKey
from app.models.user import User
from app.services.token_key_service import TokenKeyService


class TokenKeyServiceImpl(TokenKeyService):

    def create_token_key(self, user: User, db: Session, length=16):
        try:
            random_token = os.urandom(length).hex()
            new_token = TokenKeyEntity(token=random_token, user_id=user.id)
            self._delete_token_key_by_user(user, db)
            db.add(new_token)
            db.commit()
            db.refresh(new_token)
            return CommonResponseDTO.build_response(str(HTTPStatus.OK), Constants.MSG_OK, None)
        except Exception as e:
            return CommonResponseDTO.build_response(str(HTTPStatus.BAD_REQUEST), Constants.MSG_ERROR, str(e))

    def get_token_key(self, user: User, db: Session):
        try:
            token = db.query(TokenKeyEntity).filter(TokenKeyEntity.user_id == user.id).first()
            if token is None:
                return CommonResponseDTO.build_response(
                    str(HTTPStatus.NOT_FOUND),
                    Constants.MSG_NOT_FOUND,
                    None
                )
            to_json = TokenKey(**token.__dict__)
            return CommonResponseDTO.build_response(str(HTTPStatus.OK), Constants.MSG_OK, to_json.token)
        except Exception as e:
            return CommonResponseDTO.build_response(str(HTTPStatus.BAD_REQUEST), Constants.MSG_ERROR, str(e))

    def get_token_key_by_value(self, value: str, db: Session):
        try:
            token = db.query(TokenKeyEntity).filter(TokenKeyEntity.token == value).first()
            if token is None:
                return (CommonResponseDTO
                        .build_response(str(HTTPStatus.NOT_FOUND), Constants.MSG_ERROR, Constants.MSG_NOT_FOUND))
            return CommonResponseDTO.build_response(str(HTTPStatus.OK), Constants.MSG_OK, token.__dict__)
        except Exception as e:
            CommonResponseDTO.build_response(str(HTTPStatus.BAD_REQUEST), Constants.MSG_ERROR, str(e))

    @staticmethod
    def _delete_token_key_by_user(user: User, db: Session):
        try:
            get_token = db.query(TokenKeyEntity).filter(TokenKeyEntity.user_id == user.id).first()
            if get_token is None:
                return
            db.delete(get_token)
            db.commit()
        except Exception as e:
            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=Constants.MSG_ERROR)
