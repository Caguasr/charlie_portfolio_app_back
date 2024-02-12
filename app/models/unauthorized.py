from pydantic import BaseModel, Field


class Unauthorized(BaseModel):
    detail: str = Field(examples=["Not authenticated"])
