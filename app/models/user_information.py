from pydantic import BaseModel, Field


class UserInformationDTO(BaseModel):
    name: str = Field(description="Name of the user", example="username lastname")
    about: str = Field(description="About your profile", example="i am a full stack developer")
    photo: str
    position: str = Field(description="work position", example="Full Stack Developer")
    slogan: str | None = Field(description="slogan", example="I can do it!")


class UserInformation(UserInformationDTO):
    id: int = Field(description="Id of the user information", example=1)
    active: bool = Field(description="Is this user information active", example=True)
    # created_at: st = Field(description="Date and time when created the user information")

    class Config:
        from_attributes = True
