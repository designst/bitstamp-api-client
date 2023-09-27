import datetime
import decimal

from bitstamp_api.models.base import BaseResponse
from bitstamp_api.models.base import IntEnum
from bitstamp_api.models.base import RequestPayload
from bitstamp_api.models.base import StringEnum


class RippleWithdrawalRequestPayload(RequestPayload):
    """
    Ripple withdrawal request payload.
    """

    # Ripple address.
    address: str
    # Currency amount.
    amount: decimal.Decimal


class RippleWithdrawalResponse(BaseResponse):
    """
    Ripple withdrawal response.
    """

    # Withdrawal ID.
    id: int


class WithdrawalRequestRequestPayload(RequestPayload):
    """
    Withdrawal request request payload.
    """

    # Withdrawal request id.
    id: int
    # Limit result to that many withdrawal requests (minimum: 1; maximum: 1000).
    limit: int
    # Skip that many withdrawal requests before returning results (minimum: 0;
    # maximum: 200000).
    offset: int
    # Withdrawal requests from number of seconds ago to now (max. 50000000).
    timedelta: int


class WithdrawalStatus(IntEnum):
    """
    Withdrawal status.
    """

    OPEN = 0
    PROCESS = 1
    FINISHED = 2
    CANCELED = 3
    FAILED = 4


class WithdrawalType(IntEnum):
    """
    Withdrawal type.
    """

    SEPA = 0
    BTC = 1
    WIRE = 2
    XRP = 14
    LTC = 15
    ETH = 16
    BCH = 17
    PAX = 18
    XLM = 19
    LINK = 20
    OMG = 21
    USDC = 22
    AAVE = 24
    BAT = 25
    UMA = 26
    DAI = 27
    KNC = 28
    MKR = 29
    ZRX = 30
    GUSD = 31
    ALGO = 32
    AUDIO = 33
    CRV = 34
    SNX = 35
    UNI = 36
    YFI = 38
    COMP = 39
    GRT = 40
    USDT = 42
    EURT = 43
    MATIC = 46
    SUSHI = 47
    CHZ = 48
    ENJ = 49
    HBAR = 50
    ALPHA = 51
    AXS = 52
    FTT = 53
    SAND = 54
    STORJ = 55
    ADA = 56
    FET = 57
    RGT = 58
    SKL = 59
    CEL = 60
    SLP = 61
    SXP = 62
    DYDX = 65
    FTM = 66
    SHIB = 67
    AMP = 69
    GALA = 71
    PERP = 72


class WithdrawalRequestResponse(BaseResponse):
    """
    Withdrawal request response.
    """

    # Withdrawal address.
    address: str
    # Amount.
    amount: decimal.Decimal
    # Currency.
    currency: str
    # Date and time.
    datetime: datetime.datetime
    # Withdrawal ID.
    id: int
    # 0 (open), 1 (in process), 2 (finished), 3 (canceled) or 4 (failed).
    status: WithdrawalStatus
    # Transaction ID (crypto withdrawals only).
    transaction_id: str
    # Bitstamp's transaction id.
    txid: int
    # 0 (SEPA), 2 (WIRE transfer), 17 (BCH), 1 (BTC), 16 (ETH), 15 (LTC), 18 (PAX),
    # 19 (XLM), 14 (XRP), 20 (LINK), 21 (OMG), 22 (USDC), 24 (AAVE), 25 (BAT),
    # 26 (UMA), 27 (DAI), 28 (KNC), 29 (MKR), 30 (ZRX), 31 (GUSD), 32 (ALGO),
    # 33 (AUDIO), 34 (CRV), 35 (SNX), 36 (UNI), 38 (YFI), 39 (COMP), 40 (GRT),
    # 42 (USDT), 43 (EURT), 46 (MATIC), 47 (SUSHI), 48 (CHZ), 49 (ENJ), 50 (HBAR),
    # 51 (ALPHA), 52 (AXS), 53 (FTT), 54 (SAND), 55 (STORJ), 56 (ADA), 57 (FET),
    # 58 (RGT), 59 (SKL), 60 (CEL), 61 (SLP), 62 (SXP), 65 (DYDX), 66 (FTM), 67 (SHIB),
    # 69 (AMP), 71 (GALA), 72 (PERP).
    type: WithdrawalType


class CancelWithdrawalRequestPayload(RequestPayload):
    """
    Cancel withdrawal request payload.
    """

    # ID of the withdrawal request.
    id: int


class CancelWithdrawalResponse(BaseResponse):
    """
    Cancel withdrawal response.
    """

    # Account currency (balance currency from which the withdrawal was requested) of
    # the cancelled withdrawal request.
    account_currency: str
    # Amount of the cancelled withdrawal request.
    amount: decimal.Decimal
    # Currency of the cancelled withdrawal request.
    currency: str
    # ID of the cancelled withdrawal request.
    id: int
    # The type of the cancelled withdrawal request.
    type: str


class WithdrawalRequestType(StringEnum):
    """
    Withdrawal request type.
    """

    SEPA = "sepa"
    INTERNATIONAL = "international"


class OpenWithdrawalRequestPayload(RequestPayload):
    """
    Open withdrawal request payload.
    """

    # The balance from which you wish to withdraw. Can be either "USD", "EUR" or "GBP".
    amount_currency: str
    # User or company address.
    address: str
    # The amount to withdraw.
    amount: decimal.Decimal
    # Target bank address (international withdrawals only).
    bank_address: str
    # Target bank city (international withdrawals only).
    bank_city: str
    # Target bank country. Country codes must be in accordance with the ISO 3166-1
    # standard (use two character Alpha-2 codes). Disclaimer: Not all country choices
    # listed at this reference URL are supported. For a detailed list please refer to
    # our platform's withdrawal interfaces (international withdrawals only).
    bank_country: str
    # Target bank name (international withdrawals only).
    bank_name: str
    # Target bank postal code (international withdrawals only).
    bank_postal_code: str
    # The target bank BIC.
    bic: str
    # User or company city.
    city: str
    # Withdrawal comment.
    comment: str
    # User or company country. Country codes must be in accordance with the ISO 3166-1
    # standard (use two character Alpha-2 codes). Disclaimer: Not all country choices
    # listed at this reference URL are supported. For a detailed list please refer to
    # our platform's withdrawal interfaces.
    country: str
    # The currency in which the funds should be withdrawn (may involve conversion fees).
    # Currency codes must be in accordance with the ISO 4217 standard.
    # Disclaimer: Not all currency choices listed at this reference URL are supported.
    # For a detailed list please refer to our platform's withdrawal interfaces.
    # (international withdrawals only)
    currency: str
    # User or company IBAN.
    iban: str
    # Full user or company name.
    name: str
    # User or company postal code.
    postal_code: str
    # Type of the withdrawal request ("sepa" or "international").
    type: WithdrawalRequestType


class OpenWithdrawalResponse(BaseResponse):
    """
    Open withdrawal response.
    """

    # Withdrawal ID.
    withdrawal_id: int


class WithdrawalStatusRequestPayload(RequestPayload):
    """
    Withdrawal status request payload.
    """

    # ID of the withdrawal request.
    id: int


class WithdrawalStatusResponse(BaseResponse):
    """
    Withdrawal status response.
    """

    # Status of the withdrawal request.
    status: str


class CryptoWithdrawalRequestPayload(RequestPayload):
    """
    Crypto withdrawal request payload.
    """

    # Cryptocurrency address.
    address: str
    # Cryptocurrency amount.
    amount: decimal.Decimal
    # Address destination tag - applicable to: XRP.
    destination_tag: str
    # Address memo id - applicable to: XLM, HBAR.
    memo_id: str


class CryptoWithdrawalResponse(BaseResponse):
    """
    Crypto withdrawal response.
    """

    # Withdrawal ID.
    id: int
