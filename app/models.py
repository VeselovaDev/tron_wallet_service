from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class WalletQuery(Base):
    __tablename__ = "wallet_queries"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    address: Mapped[str] = mapped_column(String, index=True)
    trx_balance: Mapped[float] = mapped_column(Float)
    bandwidth: Mapped[int] = mapped_column(Integer)
    energy: Mapped[int] = mapped_column(Integer)
    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
