from datetime import datetime

from pydantic import BaseModel, Field


class RoleDTO(BaseModel):
    name: str = Field(description="name of role")


class Role(RoleDTO):
    id: int = Field(description="id role")
    created_at: datetime = Field(description="created at")
