from http import HTTPStatus
from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

from app.commons.constants.constants import Constants


class Metadata(BaseModel):
    statusCode: str = Field(description="Status code response", examples=[HTTPStatus.OK, HTTPStatus.NOT_FOUND])
    message: str = Field(description="Message response", examples=[Constants.MSG_OK, Constants.MSG_NOT_FOUND])


T = TypeVar("T")


class CommonResponseDTO(BaseModel, Generic[T]):
    metadata: Metadata = Field(description="Metadata response")
    data: T = Field(description="Response data")

    @staticmethod
    def build_response(status_code: str, message: str, data: Any):
        return CommonResponseDTO(metadata=Metadata(statusCode=status_code, message=message), data=data)
