import datetime
import decimal
import typing

from bitstamp_api.models.base import BaseResponse
from bitstamp_api.models.base import IntEnum
from bitstamp_api.models.base import StringEnum


class CurrencyType(StringEnum):
    CRYPTO = "crypto"
    FIAT = "fiat"


class CurrencyWithdrawal(StringEnum):
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class TickerSide(IntEnum):
    BUY = 0
    SELL = 1


class MarketSymbol(StringEnum):
    BTCUSD = "btcusd"


class CurrencyResponse(BaseResponse):
    available_supply: str
    currency: str
    decimals: int
    deposit: str
    logo: str
    name: str
    symbol: typing.Optional[str] = None
    type: CurrencyType
    withdrawal: CurrencyWithdrawal


class TickerHourResponse(BaseResponse):
    # Lowest sell order.
    ask: decimal.Decimal
    # Highest buy order.
    bid: decimal.Decimal
    # Last 24 hours price high.
    high: decimal.Decimal
    # Last price.
    last: decimal.Decimal
    # Last 24 hours price low.
    low: decimal.Decimal
    # First price of the day.
    open: decimal.Decimal
    # Ticker side: 0 - buy; 1 - sell.
    side: TickerSide
    # Unix timestamp date and time.
    timestamp: datetime.datetime
    # Last 24 hours volume.
    volume: decimal.Decimal
    # Last 24 hours volume weighted average price.
    vwap: decimal.Decimal


class TickerMarketResponse(BaseResponse):
    # Lowest sell order.
    ask: decimal.Decimal
    # Highest buy order.
    bid: decimal.Decimal
    # Last 24 hours price high.
    high: decimal.Decimal
    # Last price.
    last: decimal.Decimal
    # Last 24 hours price low.
    low: decimal.Decimal
    # First price of the day.
    open: decimal.Decimal
    # 24 hours time delta transaction price.
    open_24: decimal.Decimal
    # 24 hours price change percent.
    percent_change_24: typing.Optional[decimal.Decimal] = None
    # Ticker side: 0 - buy; 1 - sell.
    side: TickerSide
    # Unix timestamp date and time.
    timestamp: datetime.datetime
    # Last 24 hours volume.
    volume: decimal.Decimal
    # Last 24 hours volume weighted average price.
    vwap: decimal.Decimal


class TickerResponse(TickerMarketResponse):
    # Currency pair name.
    pair: str
