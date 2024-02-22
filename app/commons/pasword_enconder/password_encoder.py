from abc import ABC, abstractmethod

from passlib.context import CryptContext


class PasswordEncoder(ABC):
    @abstractmethod
    def hash(self, password: str) -> str:
        pass

    @abstractmethod
    def verify(self, password: str, hash_password: str) -> str:
        pass
