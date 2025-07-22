from typing import Generator, List

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session

from app import models, schemas, tron
from app.database import SessionLocal, engine
from app.models import WalletQuery

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/wallet-info/", response_model=schemas.WalletResponse)
def fetch_wallet_info(wallet: schemas.WalletRequest, db: Session = Depends(get_db)) -> schemas.WalletResponse:
    try:
        data = tron.get_wallet_info(wallet.address)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    query = WalletQuery(**data)
    db.add(query)
    db.commit()
    db.refresh(query)
    return query

@app.get("/wallet-info/", response_model=List[schemas.WalletResponse])
def get_wallets(skip: int = 0, limit: int = Query(10, le=100), db: Session = Depends(get_db)) -> List[schemas.WalletResponse]:
    return db.query(WalletQuery).order_by(WalletQuery.timestamp.desc()).offset(skip).limit(limit).all()
