from datetime import timedelta, datetime, timezone

from jose import jwt

from app.commons.constants.constants import Constants
from app.configs.environment import environment
from app.services.JWTService import JWTService

SECRET_KEY = environment.secret_key


class JWTUtil(JWTService):

    def create_access_token(self, payload: dict, expires_delta: timedelta | None = None) -> str:
        to_encode = payload.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=Constants.ALGORITHM_TOKEN)
        return encoded_jwt
