import datetime
import decimal
import typing

from bitstamp_api.models.base import BaseResponse
from bitstamp_api.models.base import IntEnum
from bitstamp_api.models.base import RequestParams
from bitstamp_api.models.base import RequestTimestamp
from bitstamp_api.models.base import StringEnum


class EurUsdResponse(BaseResponse):
    """
    EUR/USD response.
    """

    # Buy conversion rate.
    buy: decimal.Decimal
    # Sell conversion rate.
    sell: decimal.Decimal


class OhlcDataStep(IntEnum):
    """
    Timeframe in seconds.
    """

    STEP_60 = 60
    STEP_100 = 100
    STEP_300 = 300
    STEP_900 = 900
    STEP_1800 = 1800
    STEP_3600 = 3600
    STEP_7200 = 7200
    STEP_14400 = 14400
    STEP_21600 = 21600
    STEP_43200 = 43200
    STEP_86400 = 86400
    STEP_259200 = 259200


class OhlcDataRequestParams(RequestParams):
    # Unix timestamp to when OHLC data will be shown.If none from start or end
    # timestamps are posted then endpoint returns OHLC data to current unix time. If
    # both start and end timestamps are posted, end timestamp will be used.
    end: typing.Optional[RequestTimestamp] = None
    # If set, results won't include current (open) candle.
    exclude_current_candle: typing.Optional[bool] = None
    # Limit OHLC results.
    limit: int
    # Unix timestamp from when OHLC data will be started.
    start: typing.Optional[RequestTimestamp] = None
    # Timeframe in seconds.
    step: OhlcDataStep


class OhlcResponse(BaseResponse):
    # Closing price.
    close: decimal.Decimal
    # Price high.
    high: decimal.Decimal
    # Price low.
    low: decimal.Decimal
    # Opening price.
    open: decimal.Decimal
    # Unix timestamp date and time.
    timestamp: datetime.datetime
    # Volume.
    volume: decimal.Decimal


class OhlcDataDataResponse(BaseResponse):
    # OHLC data.
    ohlc: typing.List[OhlcResponse]
    # Trading pair.
    pair: str


class OhlcDataResponse(BaseResponse):
    data: OhlcDataDataResponse


class InstantAndMarketOrder(StringEnum):
    """
    Instant and market orders status (Enabled/Disabled).
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class TradingStatus(StringEnum):
    """
    Trading engine status (Enabled/Disabled).
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class TradingPairInfoResponse(BaseResponse):
    # Decimal precision for base currency (BTC/USD - base: BTC).
    base_decimals: int
    # Decimal precision for counter currency (BTC/USD - counter: USD).
    counter_decimals: int
    # Trading pair description.
    description: str
    # Instant and market orders status (Enabled/Disabled).
    instant_and_market_orders: InstantAndMarketOrder
    # Minimum order size.
    minimum_order: str
    # Trading pair.
    name: str
    # Trading engine status (Enabled/Disabled).
    trading: TradingStatus
    # URL symbol of trading pair.
    url_symbol: str
