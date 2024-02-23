from pydantic import BaseModel, Field


class TokenKey(BaseModel):
    token: str = Field(description="token to send request front external api", examples=["123123"])

    class Config:
        from_attributes = True
