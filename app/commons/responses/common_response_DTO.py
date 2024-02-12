from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field


class Metadata(BaseModel):
    statusCode: str = Field(description="Status code response", example="200")
    message: str = Field(description="Message response", example="200 OK")


T = TypeVar("T")


class CommonResponseDTO(BaseModel, Generic[T]):
    metadata: Metadata = Field(description="Metadata response")
    data: T = Field(description="Response data")

    @staticmethod
    def build_response(status_code: str, message: str, data: Any):
        return CommonResponseDTO(metadata=Metadata(statusCode=status_code, message=message), data=data)
