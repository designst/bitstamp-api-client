import typing
import urllib.parse
from enum import Enum

import requests

from bitstamp_api.exceptions import ApiException
from bitstamp_api.exceptions import BitstampException
from bitstamp_api.models.base import RequestPayload
from bitstamp_api.models.order_book import RequestParams
from bitstamp_api.models.tickers import MarketSymbol


class ApiVersion(int, Enum):
    VERSION_1 = 1
    VERSION_2 = 2


class BaseApiClient(object):
    """
    Base class of public and private api clients.
    """

    API_URL = {
        ApiVersion.VERSION_1: "https://www.bitstamp.net/api/",
        ApiVersion.VERSION_2: "https://www.bitstamp.net/api/v2/",
    }

    def _get_request(self, *args, **kwargs):
        """
        Sends a GET request.

        :return: The json-encoded content.
        :rtype: dict
        """
        return self._request(requests.get, *args, **kwargs)

    def _post_request(self, *args, **kwargs):
        """
        Sends a POST request.

        :return: The json-encoded content.
        :rtype: dict
        """
        return self._request(requests.post, *args, **kwargs)

    def _request(
        self,
        fn: typing.Callable,
        url: str,
        params: typing.Optional[RequestParams] = None,
        version: typing.Optional[ApiVersion] = None,
        *args,
        **kwargs
    ) -> typing.Optional[dict]:
        """
        Constructs and sends a :class:`Request <Request>`.

        :return: The json-encoded content.
        :rtype: dict
        """
        request_url = self._get_request_url(url, version)
        request_params = self._get_request_params(params)

        print(request_params)

        response = fn(request_url, params=request_params, *args, **kwargs)

        return self._get_json_response(response)

    def _get_request_url(
        self, url: str, version: typing.Optional[ApiVersion] = None
    ) -> str:
        """
        Returns the full request url.

        :param url: Request url.
        :param version: API version.

        :return: Full request url.
        """
        api_version = self._get_api_version(version)

        return urllib.parse.urljoin(self.API_URL[api_version], url)

    def _get_request_params(
        self, request_params: typing.Optional[RequestParams] = None
    ) -> typing.Optional[dict]:
        """
        Returns the request params.

        :param request_params: Request params.

        :return: Request params.
        """
        self._validate_request_params(request_params)

        if not request_params:
            return None

        return request_params.model_dump()

    def _get_request_payload(
        self, request_payload: typing.Optional[RequestPayload] = None
    ) -> typing.Optional[dict]:
        """
        Returns the request payload.

        :param request_payload: Request payload.

        :return: Request payload.
        """
        self._validate_request_payload(request_payload)

        if not request_payload:
            return None

        return request_payload.model_dump()

    def _get_request_payload_string(
        self,
        request_payload: typing.Optional[RequestPayload] = None,
    ) -> str:
        """
        Returns the request payload string.

        :param request_payload: Request payload.

        :return: Request payload string.
        """
        payload = self._get_request_payload(request_payload)

        if not payload:
            return ""

        return urllib.parse.urlencode(payload)

    # noinspection PyMethodMayBeStatic
    def _get_api_version(
        self, version: typing.Optional[ApiVersion] = None
    ) -> ApiVersion:
        """
        Returns the api version.

        :param version: API Version.

        :return: API Version.
        """
        if not version:
            version = ApiVersion.VERSION_2

        return version

    # noinspection PyMethodMayBeStatic
    def _get_json_response(self, response: requests.Response) -> typing.Optional[dict]:
        """
        Returns the json-encoded content of a response, if any.

        :return: The json-encoded content.
        :rtype: dict
        """
        # Check for errors and raise an exception if so.
        response.raise_for_status()

        try:
            json_response = response.json()
        except ValueError:
            json_response = None

        if isinstance(json_response, dict):
            error = json_response.get("error")

            if error:
                raise BitstampException(error)

            if json_response.get("status") == "error":
                raise BitstampException(json_response.get("reason"))

        return json_response

    # noinspection PyMethodMayBeStatic
    def _validate_market_symbol(self, market_symbol: MarketSymbol):
        """
        Validates the market symbol.

        :param market_symbol: Market symbol.

        :raise ApiException: If the market symbol is not valid.
        """
        if not isinstance(market_symbol, MarketSymbol):
            raise ApiException(
                'Parameter "market_symbol" has to be of type "MarketSymbol".'
            )

    # noinspection PyMethodMayBeStatic
    def _validate_request_params(
        self, request_params: typing.Optional[RequestParams] = None
    ):
        """
        Validates the request params.

        :param request_params: Request params.

        :raise ApiException: If the request params are not valid.
        """
        if request_params and not isinstance(request_params, RequestParams):
            raise ApiException(
                'Parameter "request_params" has to be of type "RequestParams".'
            )

    # noinspection PyMethodMayBeStatic
    def _validate_request_payload(
        self, request_payload: typing.Optional[RequestPayload] = None
    ):
        """
        Validates the request payload.

        :param request_payload: Request payload.

        :raise ApiException: If the request payload is not valid.
        """
        if request_payload and not isinstance(request_payload, RequestPayload):
            raise ApiException(
                'Parameter "request_payload" has to be of type "RequestPayload".'
            )
