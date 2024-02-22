from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.commons.responses.common_response_DTO import CommonResponseDTO
from app.models.role import RoleDTO


class RoleService(ABC):

    @abstractmethod
    def save(self, role: RoleDTO, db: Session) -> CommonResponseDTO:
        pass

    @abstractmethod
    def find_all(self, db: Session) -> CommonResponseDTO:
        pass

    @abstractmethod
    def delete(self, id_role: int, db: Session) -> CommonResponseDTO:
        pass
