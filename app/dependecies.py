from http import HTTPStatus

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from starlette import status

from app.commons.constants.constants import Constants
from app.commons.pasword_enconder.crypt import Crypt
from app.commons.responses.common_response_DTO import CommonResponseDTO
from app.configs.database import DatabaseConfig
from app.configs.environment import environment
from app.models.user import User
from app.services.services_impl.user_service_impl import UserServiceImpl
from app.services.user_service import UserService

db = DatabaseConfig(environment.db_host, environment.db_port, environment.db_username, environment.db_password,
                    environment.db_name)

secret_key = environment.secret_key


def get_db():
    session = db.create_session()
    db_session = session()
    try:
        yield db_session
    finally:
        db_session.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

crypt = Crypt()
user_service = UserServiceImpl(crypt)


async def get_current_user(token: str = Depends(oauth2_scheme), db_session: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        print(token)
        payload = jwt.decode(token, secret_key, Constants.ALGORITHM_TOKEN)
        id_user: str = payload.get("sub")
        if id_user is None:
            raise credentials_exception
    except JWTError as e:
        raise credentials_exception
    return user_service.get_user_by_id(int(id_user), db_session)


async def get_current_user_active(response: CommonResponseDTO[User] = Depends(get_current_user)):
    if response.metadata.statusCode != str(HTTPStatus.OK) or not response.data["active"]:
        raise HTTPException(
            status_code=int(response.metadata.statusCode),
            detail=response.model_dump()
        )
    return response
