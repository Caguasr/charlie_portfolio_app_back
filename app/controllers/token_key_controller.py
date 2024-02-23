from sqlalchemy.orm import Session

from app.commons.responses.common_response_DTO import CommonResponseDTO
from app.models.user import User
from app.services.token_key_service import TokenKeyService


class TokenKeyController:
    def __init__(self, token_service: TokenKeyService):
        self.token_service = token_service

    def save_token_key(self, user: User, db: Session) -> CommonResponseDTO:
        return self.token_service.create_token_key(user, db)

    def get_token_key_by_user_id(self, user: User, db: Session) -> CommonResponseDTO:
        return self.token_service.get_token_key(user, db)
