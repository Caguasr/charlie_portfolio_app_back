from datetime import datetime

from pydantic import BaseModel, Field


class UserDTO(BaseModel):
    username: str = Field(description="username user", min_length=5, examples=["user1"])
    password: str = Field(description="password user", min_length=8, exclude=True)
    role_id: int = Field(description="role id", examples=[1])


class User(UserDTO):
    id: int = Field(description="id user")
    active: bool = Field(description="active user", examples=[True])
    created_at: datetime = Field(description="date time when user created", examples=[datetime.now()])

    class Config:
        from_attributes = True
