# Bitstamp API Client

[![Python package](https://github.com/designst/bitstamp-api-client/actions/workflows/python-package.yml/badge.svg)](https://github.com/designst/bitstamp-api-client/actions/workflows/python-package.yml)
[![semantic-release: angular](https://img.shields.io/badge/semantic--release-python-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

## Install

Install from PyPI:

```shell
pip install bitstamp-api-client
```

## Getting started

How to use the public client:

```python

from bitstamp_api.clients.public import PublicApiClient
from bitstamp_api.models.tickers import MarketSymbol

public_api_client = PublicApiClient()

market_ticker = public_api_client.get_market_ticker(MarketSymbol.BTCUSD)
```

How to use the private client:

```python
from bitstamp_api.clients.private import PrivateApiClient

private_api_client = PrivateApiClient(
    key="<bitstamp-api-key>",
    secret="<bitstamp-api-secret>",
    username="<bitstamp-username>",
)

account_balances = private_api_client.get_account_balances()
```
