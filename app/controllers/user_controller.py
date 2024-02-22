from sqlalchemy.orm import Session

from app.models.user import UserDTO
from app.services.user_service import UserService


class UserController:
    def __init__(self, service: UserService):
        self._service = service

    def save(self, user: UserDTO, db: Session):
        return self._service.save(user, db)

    def find_all(self, db: Session):
        return self._service.find_all(db)

    def find_by_id(self, id_user: int, db: Session):
        return self._service.get_user_by_id(id_user, db)

    def delete_by_id(self, id_user: int, db: Session):
        return self._service.delete(id_user, db)
