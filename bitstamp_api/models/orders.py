import datetime
import decimal
import typing

from bitstamp_api.models.base import BaseResponse
from bitstamp_api.models.base import IntEnum
from bitstamp_api.models.base import RequestPayload
from bitstamp_api.models.base import StringEnum


class OrderType(IntEnum):
    """
    # 0 (buy) or 1 (sell).
    """

    BUY = 0
    SELL = 1


class BuyOrderRequestPayload(RequestPayload):
    """
    Base class for the buy order request payload.
    """

    # Amount in counter currency (Example: For BTC/USD pair, amount is quoted in USD)
    amount: decimal.Decimal
    # Unique client order id set by client. Client order id needs to be unique string.
    # Client order id value can only be used once.
    client_order_id: str


class BuyOrderResponse(BaseResponse):
    """
    Base class for the buy order response.
    """

    # Amount.
    amount: decimal.Decimal
    # Client order ID sent with request. Only returned if parameter was used in request.
    client_order_id: str
    # Date and time.
    datetime: datetime.datetime
    # Order ID.
    id: int
    # Market where the order was placed.
    market: str
    # Price.
    price: decimal.Decimal
    # 0 (buy) or 1 (sell).
    type: OrderType


class BuyInstantOrderRequestPayload(BuyOrderRequestPayload):
    """
    Buy instant order request payload.
    """


class BuyInstantOrderResponse(BuyOrderResponse):
    """
    Buy instant order response.
    """


class BuyMarketOrderRequestPayload(BuyOrderRequestPayload):
    """
    Buy market order request payload.
    """


class BuyMarketOrderResponse(BuyOrderResponse):
    """
    Buy market order response.
    """


class BuyLimitOrderRequestPayload(BuyOrderRequestPayload):
    """
    Buy limit order request payload.
    """

    # Opens buy limit order which will be canceled at 0:00 UTC unless it already has
    # been executed.
    daily_order: bool
    # Unix timestamp in milliseconds. Required in case of GTD order.
    expire_time: datetime.datetime
    # A Fill-Or-Kill (FOK) order is an order that must be executed immediately in its
    # entirety. If the order cannot be immediately executed in its entirety, it will
    # be cancelled.
    fok_order: bool
    # A Good-Till-Date (GTD) lets you select an expiration date and time up until
    # which the order will be open.
    gtd_order: bool
    # An Immediate-Or-Cancel (IOC) order is an order that must be executed immediately.
    # Any portion of an IOC order that cannot be filled immediately will be cancelled.
    ioc_order: bool
    # If the order gets executed, a new sell order will be placed, with "limit_price"
    # as its price.
    limit_price: decimal.Decimal
    # A Maker-Or-Cancel (MOC) order is an order that ensures it is not fully or
    # partially filled when placed. In case it would be, the order is cancelled.
    moc_order: bool
    # Price.
    price: decimal.Decimal


class BuyLimitOrderResponse(BuyOrderResponse):
    """
    Buy limit order response.
    """


class CancelOrderRequestPayload(RequestPayload):
    # Order ID.
    id: int


class CancelOrderResponse(BaseResponse):
    # Order amount.
    amount: decimal.Decimal
    # Order ID.
    id: int
    # Order price.
    price: decimal.Decimal
    # Order type.
    type: OrderType


class CanceledOrderResponse(CancelOrderResponse):
    # Currency pair formatted as "BTC/USD".
    currency_pair: str


class CancelAllOrdersResponse(BaseResponse):
    # Canceled orders.
    canceled: typing.List[CanceledOrderResponse]
    # "true" if all orders were successfully canceled and "false" otherwise
    success: bool


class TradingPairResponse(BaseResponse):
    # Trading pair.
    name: str
    # URL symbol of trading pair.
    url_symbol: str


class OpenOrderResponse(BaseResponse):
    # Remaining amount.
    amount: decimal.Decimal
    # Initial amount.
    amount_at_create: decimal.Decimal
    # Client order id. (Only returned if order was placed with client order id
    # parameter.)
    client_order_id: str
    # Date and time.
    datetime: datetime.datetime
    # Order ID.
    id: int
    # Limit price. (Only returned if limit order was placed with limit_price parameter.)
    limit_price: decimal.Decimal
    # Price.
    price: decimal.Decimal
    # Order type: 0 - buy; 1 - sell.
    type: OrderType


class AllOpenOrderResponse(OpenOrderResponse):
    # Currency Pair.
    currency_pair: str
    # Market where the order was placed.
    market: str


class OrderStatusRequestPayload(RequestPayload):
    # (Optional) Client order id. (Can only be used if order was placed with client
    # order id parameter.).
    client_order_id: typing.Optional[str] = None
    # Order ID.
    id: int
    # (Optional) Omits list of transactions for order ID. Possible value: True
    omit_transactions: typing.Optional[bool] = None


class OrderStatus(StringEnum):
    CANCELED = "Canceled"
    EXPIRED = "Expired"
    FINISHED = "Finished"
    OPEN = "Open"


class TransactionType(IntEnum):
    DEPOSIT = 0
    WITHDRAWAL = 1
    MARKET_TRADE = 2


class OrderTransactionResponse(BaseResponse):
    # Date and time.
    datetime: datetime.datetime
    # Transaction fee.
    fee: decimal.Decimal
    # Price.
    price: decimal.Decimal
    # Transaction ID.
    tid: int
    # Transaction type: 0 - deposit; 1 - withdrawal; 2 - market trade.
    type: TransactionType
    # {from_currency} amount.
    from_currency: str
    # {to_currency} amount.
    to_currency: str


class OrderStatusResponse(BaseResponse):
    # Amount remaining.
    amount_remaining: decimal.Decimal
    # Client order id. (Only returned if order was placed with client order id
    # parameter.).
    client_order_id: str
    # Date and time.
    datetime: datetime.datetime
    # Order ID.
    id: int
    # Market where the order was placed.
    market: str
    # Open, Finished, Expired or Canceled.
    status: OrderStatus
    # Array of objects (OrderTransaction)
    transactions: typing.List[OrderTransactionResponse]
    # Type: 0 - buy; 1 - sell.
    type: OrderType


class SellOrderRequestPayload(RequestPayload):
    """
    Base class for the sell order request payload.
    """

    # Amount in base currency (Example: For BTC/USD pair, amount is quoted in BTC)
    amount: decimal.Decimal
    # Unique client order id set by client. Client order id needs to be unique string.
    # Client order id value can only be used once.
    client_order_id: str


class SellOrderResponse(BaseResponse):
    """
    Base class for the sell order response.
    """

    # Amount.
    amount: decimal.Decimal
    # Client order ID sent with request. Only returned if parameter was used in request.
    client_order_id: str
    # Date and time.
    datetime: datetime.datetime
    # Order ID.
    id: int
    # Market where the order was placed.
    market: str
    # Price.
    price: decimal.Decimal
    # 0 (buy) or 1 (sell).
    type: OrderType


class SellInstantOrderRequestPayload(SellOrderRequestPayload):
    # (Optional) Instant sell orders allow you to sell an amount of the base currency
    # determined by the value of it in the counter-currency. Amount_in_counter sets the
    # amount parameter to refer to the counter currency instead of the base currency
    # of the selected trading pair. Possible value: True
    amount_in_counter: bool


class SellInstantOrderResponse(SellOrderResponse):
    """
    Sell instant order response.
    """


class SellMarketOrderRequestPayload(SellOrderRequestPayload):
    """
    Sell market order request payload.
    """


class SellMarketOrderResponse(SellOrderResponse):
    """
    Sell market order response.
    """


class SellLimitOrderRequestPayload(SellOrderRequestPayload):
    """
    Sell limit order request payload.
    """

    # Opens buy limit order which will be canceled at 0:00 UTC unless it already has
    # been executed.
    daily_order: bool
    # Unix timestamp in milliseconds. Required in case of GTD order.
    expire_time: datetime.datetime
    # A Fill-Or-Kill (FOK) order is an order that must be executed immediately in its
    # entirety. If the order cannot be immediately executed in its entirety, it will
    # be cancelled.
    fok_order: bool
    # A Good-Till-Date (GTD) lets you select an expiration date and time up until which
    # the order will be open.
    gtd_order: bool
    # An Immediate-Or-Cancel (IOC) order is an order that must be executed immediately.
    # Any portion of an IOC order that cannot be filled immediately will be cancelled.
    ioc_order: bool
    # If the order gets executed, a new sell order will be placed, with "limit_price"
    # as its price.
    limit_price: decimal.Decimal
    # A Maker-Or-Cancel (MOC) order is an order that ensures it is not fully or
    # partially filled when placed. In case it would be, the order is cancelled.
    moc_order: bool
    # Price.
    price: decimal.Decimal


class SellLimitOrderResponse(SellOrderResponse):
    """
    Sell limit order response.
    """
