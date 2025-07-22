from datetime import datetime, timezone
from sqlalchemy.orm import Session

from app.models import WalletQuery

def test_wallet_saved_to_db(db: Session) -> None:
    test_address: str = "TXYZ..."
    test_query = WalletQuery(
        address=test_address,
        trx_balance=10.5,
        bandwidth=300,
        energy=1500,
        timestamp=datetime.now(timezone.utc)
    )
    
    db.add(test_query)
    db.commit()

    result = db.query(WalletQuery).first()
    
    assert result is not None
    assert result.address == test_address
    assert result.trx_balance == 10.5
    assert result.bandwidth == 300
    assert result.energy == 1500
    assert isinstance(result.timestamp, datetime)
