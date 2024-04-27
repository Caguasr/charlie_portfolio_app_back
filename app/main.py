from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .commons.exceptions.common_exception import CommonException
from .configs.environment import environment
from .routers import users_information, role, user, auth, token_key

app = FastAPI(
    title="Portfolio API",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

PREFIX = environment.api_context_path


@app.exception_handler(CommonException)
async def common_exception_handler(request: Request, exc: CommonException):
    return JSONResponse(
        status_code=exc.code,
        content=exc.message
    )


app.include_router(auth.router, prefix=PREFIX)
app.include_router(token_key.router, prefix=PREFIX)
app.include_router(role.router, prefix=PREFIX)
app.include_router(user.router, prefix=PREFIX)
app.include_router(users_information.router, prefix=PREFIX)
