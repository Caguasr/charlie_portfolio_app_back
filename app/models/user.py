from datetime import datetime

from pydantic import BaseModel, Field

from app.models.role import Role


class UserBase(BaseModel):
    username: str = Field(description="username user", min_length=5, examples=["user_example"])


class UserDTO(UserBase):
    password: str = Field(description="password user", examples=["12345678"], min_length=8, exclude=True)
    role_id: int = Field(description="role id", examples=[1])


class User(UserBase):
    id: int = Field(description="id user")
    active: bool = Field(description="active user", examples=[True])
    created_at: datetime = Field(description="date time when user created", examples=[datetime.now()])
    role: Role = Field(description="role user", examples=[{"id": 1, "name": "admin", "create_at": datetime.now()}])

    class Config:
        from_attributes = True
