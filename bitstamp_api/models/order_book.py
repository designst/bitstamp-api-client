import datetime
import typing

from pydantic import BeforeValidator

from bitstamp_api.models.base import BaseResponse
from bitstamp_api.models.base import IntEnum
from bitstamp_api.models.base import RequestParams


class OrderBookGroup(IntEnum):
    """
    The group parameter is used for accessing different data from order book. Possible
    values are 0 (orders are not grouped at same price), 1 (orders are grouped at same
    price - default) or 2 (orders with their order ids are not grouped at same price).
    """

    # Orders are not grouped at same price.
    GROUP_0 = 0
    # Orders are grouped at same price - default.
    GROUP_1 = 1
    # Orders with their order ids are not grouped at same price.
    GROUP_2 = 2


def convert_microtimestamp(microtimestamp: str) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(int(microtimestamp) / 1000000)


class OrderBookRequestParams(RequestParams):
    # The group parameter is used for accessing different data from order book.
    # Possible values are 0 (orders are not grouped at same price), 1 (orders are
    # grouped at same price - default) or 2 (orders with their order ids are not
    # grouped at same price).
    group: OrderBookGroup


class OrderBookResponse(BaseResponse):
    # List of sell orders.
    asks: list[list[str]]
    # List of buy orders.
    bids: list[list[str]]
    # Unix timestamp date and time in microseconds.
    microtimestamp: typing.Annotated[
        datetime.datetime, BeforeValidator(convert_microtimestamp)
    ]
    # Unix timestamp date and time.
    timestamp: datetime.datetime
