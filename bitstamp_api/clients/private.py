import hashlib
import hmac
import time
import typing
import uuid

from bitstamp_api.clients.base import ApiVersion
from bitstamp_api.clients.base import BaseApiClient
from bitstamp_api.exceptions import ApiException
from bitstamp_api.models.account_balances import AccountBalanceResponse
from bitstamp_api.models.base import RequestPayload
from bitstamp_api.models.fees import TradingFeeResponse
from bitstamp_api.models.fees import WithdrawalFeeResponse
from bitstamp_api.models.order_book import RequestParams
from bitstamp_api.models.orders import AllOpenOrderResponse
from bitstamp_api.models.orders import BuyInstantOrderRequestPayload
from bitstamp_api.models.orders import BuyInstantOrderResponse
from bitstamp_api.models.orders import BuyLimitOrderRequestPayload
from bitstamp_api.models.orders import BuyLimitOrderResponse
from bitstamp_api.models.orders import BuyMarketOrderRequestPayload
from bitstamp_api.models.orders import BuyMarketOrderResponse
from bitstamp_api.models.orders import CancelAllOrdersResponse
from bitstamp_api.models.orders import CancelOrderRequestPayload
from bitstamp_api.models.orders import CancelOrderResponse
from bitstamp_api.models.orders import OpenOrderResponse
from bitstamp_api.models.orders import OrderStatusRequestPayload
from bitstamp_api.models.orders import OrderStatusResponse
from bitstamp_api.models.orders import SellInstantOrderRequestPayload
from bitstamp_api.models.orders import SellInstantOrderResponse
from bitstamp_api.models.orders import SellLimitOrderRequestPayload
from bitstamp_api.models.orders import SellLimitOrderResponse
from bitstamp_api.models.orders import SellMarketOrderRequestPayload
from bitstamp_api.models.orders import SellMarketOrderResponse
from bitstamp_api.models.orders import TradingPairResponse
from bitstamp_api.models.tickers import MarketSymbol
from bitstamp_api.models.transactions import CryptoTransactionRequestPayload
from bitstamp_api.models.transactions import CryptoTransactionResponse
from bitstamp_api.models.transactions import UserTransactionRequestPayload
from bitstamp_api.models.transactions import UserTransactionResponse
from bitstamp_api.models.withdrawal import CancelWithdrawalRequestPayload
from bitstamp_api.models.withdrawal import CancelWithdrawalResponse
from bitstamp_api.models.withdrawal import CryptoWithdrawalRequestPayload
from bitstamp_api.models.withdrawal import CryptoWithdrawalResponse
from bitstamp_api.models.withdrawal import OpenWithdrawalRequestPayload
from bitstamp_api.models.withdrawal import OpenWithdrawalResponse
from bitstamp_api.models.withdrawal import RippleWithdrawalRequestPayload
from bitstamp_api.models.withdrawal import RippleWithdrawalResponse
from bitstamp_api.models.withdrawal import WithdrawalRequestRequestPayload
from bitstamp_api.models.withdrawal import WithdrawalRequestResponse
from bitstamp_api.models.withdrawal import WithdrawalStatusRequestPayload
from bitstamp_api.models.withdrawal import WithdrawalStatusResponse


class PrivateApiClient(BaseApiClient):
    """
    Private api functions.
    """

    def __init__(self, key, secret, username, *args, **kwargs):
        super(PrivateApiClient, self).__init__(*args, **kwargs)

        self.key = key
        self.secret = secret
        self.username = username

    def get_account_balances(self) -> typing.List[AccountBalanceResponse]:
        """
        Return account balances.

        :return: Account balances.
        """
        response_list = self._post_request("account_balances/")

        return [AccountBalanceResponse(**response) for response in response_list]

    def get_account_balances_for_currency(
        self,
        currency: str,
    ) -> AccountBalanceResponse:
        """
        Return account balances for currency.

        :param currency: Requested currency.

        :return: Account balances for currency.
        """
        response = self._post_request(f"account_balances/{currency}/")

        return AccountBalanceResponse(**response)

    def get_trading_fees(self) -> typing.List[TradingFeeResponse]:
        """
        Return all trading fees.

        :return: All trading fees.
        """
        response_list = self._post_request("fees/trading/")

        return [TradingFeeResponse(**response) for response in response_list]

    def get_trading_fees_for_currency(
        self,
        market_symbol: MarketSymbol,
    ) -> TradingFeeResponse:
        """
        Return trading fees for currency.

        :param market_symbol: Requested currency pair.

        :return: Trading fees for currency.
        """
        self._validate_market_symbol(market_symbol)

        response = self._post_request(f"fees/trading/{market_symbol.value}/")

        return TradingFeeResponse(**response)

    def get_withdrawal_fees(self) -> typing.List[WithdrawalFeeResponse]:
        """
        Return withdrawal fees.

        :return: Withdrawal fees.
        """
        response_list = self._post_request("fees/withdrawal/")

        return [WithdrawalFeeResponse(**response) for response in response_list]

    def get_withdrawal_fees_for_currency(
        self,
        currency: str,
    ) -> WithdrawalFeeResponse:
        """
        Return withdrawal fee for currency.

        :param currency: Requested currency.

        :return: Withdrawal fee for currency.
        """
        response = self._post_request(f"fees/withdrawal/{currency}/")

        return WithdrawalFeeResponse(**response)

    def buy_instant_order(
        self,
        market_symbol: MarketSymbol,
        request_payload: BuyInstantOrderRequestPayload,
    ) -> BuyInstantOrderResponse:
        """
        Open a buy instant order. By placing an instant order you acknowledge that the
        execution of your order depends on the market conditions and that these
        conditions may be subject to sudden changes that cannot be foreseen. This call
        will be executed on the account (Sub or Main), to which the used API key is
        bound to.

        :param market_symbol: Requested currency pair.
        :param request_payload: Request payload.

        :return: Buy instant order.
        """
        self._validate_market_symbol(market_symbol)

        response = self._post_request(
            f"buy/instant/{market_symbol.value}/", payload=request_payload
        )

        return BuyInstantOrderResponse(**response)

    def buy_market_order(
        self,
        market_symbol: MarketSymbol,
        request_payload: BuyMarketOrderRequestPayload,
    ) -> BuyMarketOrderResponse:
        """
        Open a buy market order. By placing a market order you acknowledge that the
        execution of your order depends on the market conditions and that these
        conditions may be subject to sudden changes that cannot be foreseen. This call
        will be executed on the account (Sub or Main), to which the used API key is
        bound to.

        :param market_symbol: Requested currency pair.
        :param request_payload: Request payload.

        :return: Buy market order.
        """
        self._validate_market_symbol(market_symbol)

        response = self._post_request(
            f"buy/market/{market_symbol.value}/", payload=request_payload
        )

        return BuyMarketOrderResponse(**response)

    def buy_limit_order(
        self, market_symbol: MarketSymbol, request_payload: BuyLimitOrderRequestPayload
    ) -> BuyLimitOrderResponse:
        """
        Open a buy limit order. This call will be executed on the account (Sub or Main),
        to which the used API key is bound to.

        :param market_symbol: Requested currency pair.
        :param request_payload: Request payload.

        :return: Buy limit order.
        """
        self._validate_market_symbol(market_symbol)

        response = self._post_request(
            f"buy/{market_symbol.value}/", payload=request_payload
        )

        return BuyLimitOrderResponse(**response)

    def cancel_all_orders(self) -> CancelAllOrdersResponse:
        """
        Cancel all open orders. This call will be executed on the account (Sub or Main),
        to which the used API key is bound to.

        :return: Canceled orders.
        """
        response = self._post_request("cancel_all_orders/")

        return CancelAllOrdersResponse(**response)

    def cancel_all_orders_for_currency(
        self,
        market_symbol: MarketSymbol,
    ) -> CancelAllOrdersResponse:
        """
        Cancel all open orders for a currency pair. This call will be executed on the
        account (Sub or Main), to which the used API key is bound to.

        :param market_symbol: Requested currency pair.

        :return:  Canceled orders.
        """
        self._validate_market_symbol(market_symbol)

        response = self._post_request(f"cancel_all_orders/{market_symbol.value}/")

        return CancelAllOrdersResponse(**response)

    def cancel_order(
        self,
        request_payload: CancelOrderRequestPayload,
    ) -> CancelOrderResponse:
        """
        Cancel an order. This call will be executed on the account (Sub or Main), to
        which the used API key is bound to.

        :param request_payload: Request payload.

        :return: Canceled order.
        """
        response = self._post_request("cancel_order/", payload=request_payload)

        return CancelOrderResponse(**response)

    def get_trading_pairs(self) -> typing.List[TradingPairResponse]:
        """
        Returns all trading pairs that can be traded on selected account.

        :return: All trading pairs.
        """
        response_list = self._get_request("my_trading_pairs/")

        return [TradingPairResponse(**response) for response in response_list]

    def get_all_open_orders(self) -> typing.List[AllOpenOrderResponse]:
        """
        Return user's open orders. This API call is cached for 10 seconds. This call
        will be executed on the account (Sub or Main), to which the used API key is
        bound to.

        :return: All open orders.
        """
        response_list = self._post_request("open_orders/all/")

        return [AllOpenOrderResponse(**response) for response in response_list]

    def get_open_orders(
        self,
        market_symbol: MarketSymbol,
    ) -> typing.List[OpenOrderResponse]:
        """
        Return user's open orders for currency pair. This API call is cached for 10
        seconds. This call will be executed on the account (Sub or Main), to which the
        used API key is bound to.

        :param market_symbol: Requested currency pair.

        :return: Open orders for currency pair.
        """
        self._validate_market_symbol(market_symbol)

        response_list = self._post_request(f"open_orders/{market_symbol.value}/")

        return [OpenOrderResponse(**response) for response in response_list]

    def get_order_status(
        self,
        request_payload: OrderStatusRequestPayload,
    ) -> OrderStatusResponse:
        """
        Returns order status. This call will be executed on the account (Sub or Main),
        to which the used API key is bound to. Order can be fetched by using either id
        or client_order_id parameter. For closed orders, this call only returns
        information for the last 30 days. 'Order not found' error will be returned for
        orders outside this time range.

        :param request_payload: Request payload.

        :return: Order status.
        """
        response = self._post_request("order_status/", payload=request_payload)

        return OrderStatusResponse(**response)

    def sell_instant_order(
        self,
        market_symbol: MarketSymbol,
        request_payload: SellInstantOrderRequestPayload,
    ) -> SellInstantOrderResponse:
        """
        Open an instant sell order. By placing an instant order you acknowledge that
        the execution of your order depends on the market conditions and that these
        conditions may be subject to sudden changes that cannot be foreseen. This call
        will be executed on the account (Sub or Main), to which the used API key is
        bound to.

        :param market_symbol: Requested currency pair.
        :param request_payload: Request payload.

        :return: Instant sell order.
        """
        self._validate_market_symbol(market_symbol)

        response = self._post_request(
            f"sell/instant/{market_symbol.value}/", payload=request_payload
        )

        return SellInstantOrderResponse(**response)

    def sell_market_order(
        self,
        market_symbol: MarketSymbol,
        request_payload: SellMarketOrderRequestPayload,
    ) -> SellMarketOrderResponse:
        """
        Open a sell market order. By placing a market order you acknowledge that the
        execution of your order depends on the market conditions and that these
        conditions may be subject to sudden changes that cannot be foreseen. This call
        will be executed on the account (Sub or Main), to which the used API key is
        bound to.

        :param market_symbol: Requested currency pair.
        :param request_payload: Request payload.

        :return: Sell market order.
        """
        self._validate_market_symbol(market_symbol)

        response = self._post_request(
            f"sell/market/{market_symbol.value}/", payload=request_payload
        )

        return SellMarketOrderResponse(**response)

    def sell_limit_order(
        self,
        market_symbol: MarketSymbol,
        request_payload: SellLimitOrderRequestPayload,
    ) -> SellLimitOrderResponse:
        """
        Open a sell limit order. This call will be executed on the account
        (Sub or Main), to which the used API key is bound to.

        :param market_symbol: Requested currency pair.
        :param request_payload: Request payload.

        :return: Sell limit order.
        """
        self._validate_market_symbol(market_symbol)

        response = self._post_request(
            f"sell/{market_symbol.value}/", payload=request_payload
        )

        return SellLimitOrderResponse(**response)

    def ripple_withdrawal(
        self,
        request_payload: RippleWithdrawalRequestPayload,
    ) -> RippleWithdrawalResponse:
        """
        This call will be executed on the account (Sub or Main), to which the used API
        key is bound to. This endpoint supports withdrawals of USD, BTC or EUR* IOU on
        the XRP Ledger.

        *IOUs are supported globally except for Singapore. Also, EUR-IOUs are not
        supported in the US.

        :param request_payload: Request payload.

        :return: Ripple withdrawal.
        """
        response = self._post_request("ripple_withdrawal/", payload=request_payload)

        return RippleWithdrawalResponse(**response)

    def get_withdrawal_requests(
        self,
        request_payload: WithdrawalRequestRequestPayload,
    ) -> WithdrawalRequestResponse:
        """
        Return user's withdrawal requests. This call will be executed on the account
        (Sub or Main), to which the used API key is bound to.

        :param request_payload: Request payload.

        :return: Withdrawal requests.
        """
        response = self._post_request("withdrawal-requests/", payload=request_payload)

        return WithdrawalRequestResponse(**response)

    def cancel_withdrawal(
        self,
        request_payload: CancelWithdrawalRequestPayload,
    ) -> CancelWithdrawalResponse:
        """
        Cancels a bank or crypto withdrawal request. This call can only be performed by
        your Main Account.

        :param request_payload: Request payload.

        :return: Cancel withdrawal.
        """
        response = self._post_request("withdrawal/cancel/", payload=request_payload)

        return CancelWithdrawalResponse(**response)

    def open_withdrawal(
        self,
        request_payload: OpenWithdrawalRequestPayload,
    ) -> OpenWithdrawalResponse:
        """
        Opens a bank withdrawal request (SEPA or international). Withdrawal requests
        opened via API are automatically confirmed (no confirmation e-mail will be
        sent), but are processed just like withdrawals opened through the platform's
        interface. This call can only be performed by your Main Account.

        :param request_payload: Request payload.

        :return: Withdrawal request.
        """
        response = self._post_request("withdrawal/open/", payload=request_payload)

        return OpenWithdrawalResponse(**response)

    def get_withdrawal_status(
        self, request_payload: WithdrawalStatusRequestPayload
    ) -> WithdrawalStatusResponse:
        """
        Checks the status of a fiat withdrawal request. This call can only be performed
        by your Main Account.

        :param request_payload: Request payload.

        :return: Withdrawal request status.
        """
        response = self._post_request("withdrawal/status/", payload=request_payload)

        return WithdrawalStatusResponse(**response)

    def crypto_withdrawal(
        self,
        currency: str,
        request_payload: CryptoWithdrawalRequestPayload,
    ) -> CryptoWithdrawalResponse:
        """
        Request a crypto withdrawal.

        :param currency: Currency.
        :param request_payload: Request payload.

        :return: Withdrawal request.
        """
        response = self._post_request(
            f"{currency}_withdrawal/", payload=request_payload
        )

        return CryptoWithdrawalResponse(**response)

    def get_crypto_transactions(
        self,
        request_payload: typing.Optional[CryptoTransactionRequestPayload] = None,
    ) -> CryptoTransactionResponse:
        """
        Return user's crypto transactions. This call will be executed on the account,
        to which the used API key is bound to. This call is for your main account only.

        :param request_payload: Request payload.

        :return: Crypto transactions.
        """
        response = self._post_request("crypto-transactions/", payload=request_payload)

        return CryptoTransactionResponse(**response)

    def get_user_transactions(
        self,
        request_payload: typing.Optional[UserTransactionRequestPayload] = None,
    ) -> typing.List[UserTransactionResponse]:
        """
        Return user transactions from a given time frame. This call will be executed on
        the account (Sub or Main), to which the used API key is bound to.

        :param request_payload: Request payload.

        :return: User transactions.
        """
        response_list = self._post_request(
            "user_transactions/", payload=request_payload
        )

        return [UserTransactionResponse(**response) for response in response_list]

    def get_user_transactions_for_currency(
        self,
        market_symbol: MarketSymbol,
        request_payload: typing.Optional[UserTransactionRequestPayload] = None,
    ) -> typing.List[UserTransactionResponse]:
        """
        Return user transactions for a currency pair from a given time frame. This call
        will be executed on the account (Sub or Main), to which the used API key is
        bound to.

        :param market_symbol: Requested currency pair.
        :param request_payload: Request payload.

        :return: User transactions.
        """
        response_list = self._post_request(
            f"user_transactions/{market_symbol.value}/", payload=request_payload
        )

        return [UserTransactionResponse(**response) for response in response_list]

    def _request(
        self,
        fn: typing.Callable,
        url: str,
        params: typing.Optional[RequestParams] = None,
        payload: typing.Optional[RequestPayload] = None,
        version: typing.Optional[ApiVersion] = None,
        *args,
        **kwargs,
    ):
        nonce = str(uuid.uuid4())
        timestamp = str(int(round(time.time() * 1000)))
        api_version = self._get_api_version(version)
        content_type = "application/x-www-form-urlencoded"

        request_url = self._get_request_url(url, version)
        request_params = self._get_request_params(params)
        request_payload_string = self._get_request_payload_string(payload)

        request_url_without_scheme = request_url.replace("https://", "")

        content_type_message = content_type if request_payload_string else ""

        # '' (empty string) in message represents any query parameters or an empty
        # string in case there are none
        message = (
            f"BITSTAMP {self.key}POST{request_url_without_scheme}{content_type_message}"
            f"{nonce}{timestamp}v{api_version.value}{request_payload_string}"
        ).encode("utf-8")

        secret_bytes = bytes(self.secret, "utf-8")

        signature = hmac.new(
            secret_bytes, msg=message, digestmod=hashlib.sha256
        ).hexdigest()

        headers = {
            "X-Auth": f"BITSTAMP {self.key}",
            "X-Auth-Nonce": nonce,
            "X-Auth-Signature": signature,
            "X-Auth-Timestamp": timestamp,
            "X-Auth-Version": f"v{api_version.value}",
        }

        if request_payload_string:
            headers["Content-Type"] = content_type

        response = fn(
            request_url,
            data=request_payload_string,
            params=request_params,
            headers=headers,
            *args,
            **kwargs,
        )

        if not response.status_code == 200:
            raise ApiException("Status code not 200")

        response_content_type = response.headers.get("Content-Type")

        string_to_sign = (nonce + timestamp + response_content_type).encode(
            "utf-8"
        ) + response.content

        signature_check = hmac.new(
            secret_bytes, msg=string_to_sign, digestmod=hashlib.sha256
        ).hexdigest()

        if response.headers.get("X-Server-Auth-Signature") != signature_check:
            raise ApiException("Signatures do not match")

        return self._get_json_response(response)
