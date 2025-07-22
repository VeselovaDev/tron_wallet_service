from datetime import datetime
from pydantic import BaseModel, Field


class WalletRequest(BaseModel):
    address: str = Field(..., json_schema_extra={"example": "TXYZ1234567890"})

class WalletResponse(BaseModel):
    address: str
    trx_balance: float
    bandwidth: int
    energy: int
    timestamp: datetime

    model_config = {
        "from_attributes": True
    }
