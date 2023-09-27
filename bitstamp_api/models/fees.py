import decimal

from bitstamp_api.models.base import BaseResponse


class TradingFee(BaseResponse):
    """
    Trading fee.
    """

    # Fee for maker of the market.
    maker: decimal.Decimal
    # Fee for taker of the market.
    taker: decimal.Decimal


class TradingFeeResponse(BaseResponse):
    """
    Trading fee response.
    """

    # Currency pair name. (deprecated)
    currency_pair: str
    # Dictionary of maker and taker fees.
    fees: TradingFee
    # Market for fees.
    market: str


class WithdrawalFeeResponse(BaseResponse):
    """
    Withdrawal fee response.
    """

    # Currency name.
    currency: str
    # Customer withdrawal fee.
    fee: decimal.Decimal
