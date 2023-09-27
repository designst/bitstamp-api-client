import typing

from bitstamp_api.clients.base import BaseApiClient
from bitstamp_api.models.base import ErrorResponse
from bitstamp_api.models.market_info import EurUsdResponse
from bitstamp_api.models.market_info import OhlcDataRequestParams
from bitstamp_api.models.market_info import OhlcDataResponse
from bitstamp_api.models.market_info import TradingPairInfoResponse
from bitstamp_api.models.order_book import OrderBookRequestParams
from bitstamp_api.models.order_book import OrderBookResponse
from bitstamp_api.models.tickers import CurrencyResponse
from bitstamp_api.models.tickers import MarketSymbol
from bitstamp_api.models.tickers import TickerHourResponse
from bitstamp_api.models.tickers import TickerMarketResponse
from bitstamp_api.models.tickers import TickerResponse
from bitstamp_api.models.transactions import TransactionRequestParams
from bitstamp_api.models.transactions import TransactionResponse


class PublicApiClient(BaseApiClient):
    """
    Public api functions.
    """

    def get_currencies(self) -> typing.List[CurrencyResponse]:
        """
        Returns list of all currencies with basic data.


        :return: List of all currencies with basic data.
        """
        response_list = self._get_request("currencies/")

        return [CurrencyResponse(**response) for response in response_list]

    def get_ticker(self) -> typing.List[TickerResponse]:
        """
        Return ticker data for all currency pairs. Passing any GET parameters, will
        result in your request being rejected.

        :return: Ticker data for all currency pairs.
        """
        response_list = self._get_request("ticker/")

        return [TickerResponse(**response) for response in response_list]

    def get_market_ticker(
        self,
        market_symbol: MarketSymbol,
    ) -> TickerMarketResponse:
        """
        Return ticker data for the requested currency pair. Passing any GET parameters,
        will result in your request being rejected.

        :param market_symbol: Requested currency pair.

        :return: Ticker data for the requested currency pair.
        """
        self._validate_market_symbol(market_symbol)

        response = self._get_request(f"ticker/{market_symbol.value}/")

        return TickerMarketResponse(**response)

    def get_hourly_ticker(
        self,
        market_symbol: MarketSymbol,
    ) -> TickerHourResponse:
        """
        Return hourly ticker data for the requested currency pair. Passing any GET
        parameters, will result in your request being rejected.

        :param market_symbol: Requested currency pair.

        :return: Hourly ticker data for the requested currency pair.
        """
        self._validate_market_symbol(market_symbol)

        response = self._get_request(f"ticker_hour/{market_symbol.value}/")

        return TickerHourResponse(**response)

    def get_order_book(
        self,
        market_symbol: MarketSymbol,
        request_params: typing.Optional[OrderBookRequestParams] = None,
    ) -> typing.Union[OrderBookResponse, ErrorResponse]:
        """
        Returns order book data.

        :param market_symbol: Requested currency pair.
        :param request_params: Request parameters.

        :return: Order book data.
        """
        self._validate_market_symbol(market_symbol)

        response = self._get_request(
            f"order_book/{market_symbol.value}/", params=request_params
        )

        return OrderBookResponse(**response)

    def get_transactions(
        self,
        market_symbol: MarketSymbol,
        request_params: typing.Optional[TransactionRequestParams] = None,
    ) -> typing.List[TransactionResponse]:
        """
        Return transaction data from a given time frame.

        :param market_symbol: Requested currency pair.
        :param request_params: Request parameters.

        :return: Transaction data for a given time frame.
        """
        self._validate_market_symbol(market_symbol)

        response_list = self._get_request(
            f"transactions/{market_symbol.value}/", params=request_params
        )

        return [TransactionResponse(**response) for response in response_list]

    def get_eur_usd(self) -> EurUsdResponse:
        """
        Return EUR/USD conversion rate.

        :return: EUR/USD conversion rate.
        """
        response = self._get_request("eur_usd/")

        return EurUsdResponse(**response)

    def get_ohlc_data(
        self,
        market_symbol: MarketSymbol,
        request_params: OhlcDataRequestParams,
    ) -> OhlcDataResponse:
        """
        Returns OHLC (Open High Low Close) data.

        :return: OHLC (Open High Low Close) data.
        """
        self._validate_market_symbol(market_symbol)

        response = self._get_request(
            f"ohlc/{market_symbol.value}/", params=request_params
        )

        return OhlcDataResponse(**response)

    def get_trading_pairs_info(self) -> typing.List[TradingPairInfoResponse]:
        """
        Return trading pairs info.

        :return: Trading pairs info.
        """
        response_list = self._get_request("trading-pairs-info/")

        return [TradingPairInfoResponse(**response) for response in response_list]
