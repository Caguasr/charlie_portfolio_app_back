from sqlalchemy.orm import Session

from app.models.role import RoleDTO
from app.services.role_service import RoleService


class RoleController:
    def __init__(self, service: RoleService):
        self.service = service

    def save(self, role: RoleDTO, db: Session):
        return self.service.save(role, db)
