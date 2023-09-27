import decimal

from bitstamp_api.models.base import BaseResponse


class AccountBalanceResponse(BaseResponse):
    """
    Account balance response.
    """

    # Available balance for trading.
    available: decimal.Decimal
    # Currency name.
    currency: str
    # Reserved balance for trading.
    reserved: decimal.Decimal
    # Total balance on exchange.
    total: decimal.Decimal
