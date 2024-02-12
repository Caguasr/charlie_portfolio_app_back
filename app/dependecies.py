from http import HTTPStatus

from fastapi.security import OAuth2PasswordBearer

from app.commons.constants.constants import Constants
from app.commons.responses.common_response_DTO import CommonResponseDTO
from app.configs.database import DatabaseConfig
from app.configs.environment import environment

db = DatabaseConfig(environment.db_host, environment.db_port, environment.db_username, environment.db_password,
                    environment.db_name)


def get_db():
    session = db.create_session()
    db_session = session()
    try:
        yield db_session
    finally:
        db_session.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
