from pydantic import BaseModel, Field


class AuthDTO(BaseModel):
    username: str = Field(description="Username", example="user1")
    password: str = Field(description="Password", example="12345678")


class AuthToken(BaseModel):
    access_token: str = Field(description="Token",
                              example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNoYXJsaWUiLCJleHAiOjE3MDg1MzE5MTh9.BAbk2yrEEuoZ_uMdTNcTmOW9LlrX12EDbbJ8UpEpcbM")
    token_type: str = Field(description="Token Type", example="bearer")
