import datetime
from enum import Enum
from typing import Annotated

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import PlainSerializer

RequestTimestamp = Annotated[
    datetime.datetime,
    PlainSerializer(
        lambda value: int(round(value.timestamp())),
        when_used="always",
        return_type=float,
    ),
]


class IntEnum(int, Enum):
    """
    Int enum base class.
    """


class StringEnum(str, Enum):
    """
    String enum base class.
    """


class RequestParams(BaseModel):
    """
    Base class for all request params models.
    """

    model_config = ConfigDict(
        strict=True,
        use_enum_values=True,
    )


class RequestPayload(BaseModel):
    """
    Base class for all request payload models.
    """


class BaseResponse(BaseModel):
    """
    Base class for all response models.
    """


class ErrorResponse(BaseModel):
    """
    Error response.
    """

    # Error reason.
    reason: str
    # Error status.
    status: str
