import datetime
import decimal
import typing

from bitstamp_api.models.base import BaseResponse
from bitstamp_api.models.base import IntEnum
from bitstamp_api.models.base import RequestParams
from bitstamp_api.models.base import RequestPayload
from bitstamp_api.models.base import StringEnum


class TransactionTime(StringEnum):
    """
    The time interval from which we want the transactions to be returned. Possible
    values are minute, hour (default) or day.
    """

    DAY = "day"
    HOUR = "hour"
    MINUTE = "minute"


class TransactionType(IntEnum):
    """
    0 (buy) or 1 (sell).
    """

    BUY = 0
    SELL = 1


class TransactionRequestParams(RequestParams):
    # The time interval from which we want the transactions to be returned. Possible
    # values are minute, hour (default) or day.
    time: TransactionTime


class TransactionResponse(BaseResponse):
    # Amount.
    amount: decimal.Decimal
    # Unix timestamp date and time.
    date: datetime.datetime
    # Price.
    price: decimal.Decimal
    # Transaction ID.
    tid: int
    # 0 (buy) or 1 (sell).
    type: TransactionType


class CryptoTransactionRequestPayload(RequestPayload):
    """
    Crypto transaction request payload.
    """

    # True - shows also ripple IOU transactions.
    include_ious: bool
    # Limit result to that many transactions (default: 100; maximum: 1000).
    limit: int
    # Skip that many transactions before returning results (default: 0,
    # maximum: 200000).
    offset: int


class CryptoTransaction(BaseResponse):
    """
    Crypto transaction.
    """

    # Amount.
    amount: decimal.Decimal
    # Currency.
    currency: str
    # Destination address.
    destinationAddress: typing.Optional[str] = None
    # Transaction hash.
    txid: str


class CryptoTransactionResponse(BaseResponse):
    """
    Crypto transaction response.
    """

    # Deposits.
    deposits: typing.Optional[typing.List[CryptoTransaction]] = None
    # Ripple IOU transactions.
    ripple_iou_transactions: typing.Optional[typing.List[CryptoTransaction]] = None
    # Withdrawals.
    withdrawals: typing.Optional[typing.List[CryptoTransaction]] = None


class Sort(StringEnum):
    """
    Sort.
    """

    ASCENDING = "asc"
    DESCENDING = "desc"


class UserTransactionRequestPayload(RequestPayload):
    """
    User transaction request payload.
    """

    # Limit result to that many transactions (default: 100; maximum: 1000).
    limit: int
    # Skip that many transactions before returning results (default: 0,
    # maximum: 200000). If you need to export older history contact support OR use
    # combination of limit and since_id parameters.
    offset: int
    # (Optional) Show only transactions from specified transaction id. If since_id
    # parameter is used, limit parameter is set to 1000.
    since_id: int
    # (Optional) Show only transactions from unix timestamp (for max 30 days old).
    since_timestamp: datetime.datetime
    # Sorting by date and time: asc - ascending; desc - descending (default: desc).
    sort: Sort
    # Show only transactions to unix timestamp (for max 30 days old).
    until_timestamp: datetime.datetime


class UserTransactionType(IntEnum):
    """
    User transaction type.
    """

    DEPOSIT = 0
    WITHDRAWAL = 1
    MARKET_TRADE = 2
    SUB_ACCOUNT_TRANSFER = 14
    CREDITED_WITH_STAKED_ASSETS = 25
    SENT_ASSETS_TO_STAKING = 26
    STAKING_REWARD = 27
    REFERRAL_REWARD = 32
    SETTLEMENT_TRANSFER = 33
    INTER_ACCOUNT_TRANSFER = 35


class UserTransactionResponse(BaseResponse):
    """
    User transaction response.
    """

    # Date and time.
    datetime: datetime.datetime
    # Transaction fee.
    fee: decimal.Decimal
    # Transaction ID.
    id: int
    # Executed order ID.
    order_id: int
    # True if transaction is a self trade transaction.
    self_trade: bool
    # Order ID of the complementary order of the self trade.
    self_trade_order_id: int
    # Transaction type: 0 - deposit; 1 - withdrawal; 2 - market trade;
    # 14 - sub account transfer; 25 - credited with staked assets;
    # 26 - sent assets to staking; 27 - staking reward; 32 - referral reward;
    # 35 - inter account transfer; 33 - settlement transfer.
    type: UserTransactionType
    # {currency_pair} exchange rate.
    currency_pair: str
    # {from_currency} amount.
    from_currency: str
    # {to_currency} amount.
    to_currency: str
