import datetime
import decimal
import typing
import unittest
from unittest.mock import Mock
from unittest.mock import patch

import requests
from pydantic import BaseModel

from bitstamp_api.clients.public import PublicApiClient
from bitstamp_api.models.tickers import TickerResponse
from bitstamp_api.models.tickers import TickerSide


class PublicApiClientTests(unittest.TestCase):
    """ """

    def setUp(self) -> None:
        self.public_api_client = PublicApiClient()

    # noinspection PyMethodMayBeStatic
    def _mock_response(
        self,
        mock_request: typing.Union[requests.get, requests.post],
        response: typing.Union[BaseModel, typing.List[BaseModel]],
    ):
        mock_response = Mock()

        if isinstance(response, list):
            return_value = [_response.model_dump() for _response in response]
        else:
            return_value = response.model_dump()

        mock_response.json.return_value = return_value
        mock_request.return_value = mock_response

    @patch("requests.get")
    def test_get_ticker(self, mock_get):
        response = [
            TickerResponse(
                ask=decimal.Decimal("1.00"),
                bid=decimal.Decimal("2.00"),
                high=decimal.Decimal("3.00"),
                last=decimal.Decimal("4.00"),
                low=decimal.Decimal("5.00"),
                open=decimal.Decimal("6.00"),
                open_24=decimal.Decimal("7.00"),
                pair="btc",
                percent_change_24=decimal.Decimal("8.00"),
                side=TickerSide.BUY,
                timestamp=datetime.datetime.utcnow().timestamp(),
                volume=decimal.Decimal("9.00"),
                vwap=decimal.Decimal("10.00"),
            ),
        ]

        self._mock_response(mock_get, response)

        ticker = self.public_api_client.get_ticker()

        mock_get.assert_called_with(
            "https://www.bitstamp.net/api/v2/ticker/", params=None
        )

        self.assertEqual(response, ticker)
