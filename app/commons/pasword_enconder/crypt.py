from passlib.context import CryptContext

from app.commons.pasword_enconder.password_encoder import PasswordEncoder

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Crypt(PasswordEncoder):
    def hash(self, password: str) -> str:
        return pwd_context.hash(password)

    def verify(self, password: str, hash_password: str) -> bool:
        return pwd_context.verify(password, hash_password)
