from abc import ABC, abstractmethod
from datetime import timedelta


class JWTService(ABC):
    @abstractmethod
    def create_access_token(self, payload: dict, expires_delta: timedelta | None = None) -> str:
        pass
