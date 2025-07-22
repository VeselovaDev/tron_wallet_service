from datetime import datetime, timezone
from typing import TypedDict

from tronpy import Tron


class WalletInfoDict(TypedDict):
    address: str
    trx_balance: float
    bandwidth: int
    energy: int
    timestamp: datetime


def get_wallet_info(address: str) -> WalletInfoDict:
    client = Tron()
    acc_info = client.get_account(address)
    resource = client.get_account_resource(address)
    bandwidth = resource['free_net_remaining']
    energy = resource['EnergyRemaining']
    trx_balance = acc_info.get('balance', 0) / 1_000_000  # Convert from sun to TRX
    timestamp = datetime.now(timezone.utc)

    return {
        "address": address,
        "trx_balance": trx_balance,
        "bandwidth": bandwidth,
        "energy": energy,
        "timestamp": timestamp
    }
