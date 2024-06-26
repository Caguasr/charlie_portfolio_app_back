from datetime import datetime

from pydantic import BaseModel, Field


class RoleDTO(BaseModel):
    name: str = Field(description="name of role")


class Role(RoleDTO):
    id: int = Field(description="id role")
    created_at: datetime | None = Field(description="created at")

    class Config:
        from_attributes: True
