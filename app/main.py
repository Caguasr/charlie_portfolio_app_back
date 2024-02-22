from fastapi import FastAPI, Depends

from . import entities
from .configs.database import DatabaseConfig
from .dependecies import get_db, oauth2_scheme
from .routers import users_information, role, user, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Portfolio API",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth.router, dependencies=[Depends(get_db)])
app.include_router(role.router, dependencies=[Depends(get_db), Depends(oauth2_scheme)])
app.include_router(user.router, dependencies=[Depends(get_db), Depends(oauth2_scheme)])
app.include_router(users_information.router, dependencies=[Depends(get_db), Depends(oauth2_scheme)])
