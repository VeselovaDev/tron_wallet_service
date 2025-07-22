from datetime import datetime, timezone
from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app import main, tron
from app.models import Base


def mocked_get_wallet_info(address: str) -> dict[str, object]:
    return {
        "address": address,
        "trx_balance": 100.0,
        "bandwidth": 500,
        "energy": 2000,
        "timestamp": datetime(2025, 7, 22, 10, 0, 0, tzinfo=timezone.utc)
    }


@pytest.fixture(autouse=True)
def patch_get_wallet_info(monkeypatch) -> None:
    monkeypatch.setattr(tron, "get_wallet_info", mocked_get_wallet_info)


TEST_DATABASE_URL = "sqlite:///./test_wallet_info.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db() -> Generator[Session, None, None]:
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db: Session) -> Generator[TestClient, None, None]:
    def override_get_db() -> Generator[Session, None, None]:
        try:
            yield db
        finally:
            pass

    main.app.dependency_overrides[main.get_db] = override_get_db
    with TestClient(main.app) as c:
        yield c
    main.app.dependency_overrides.clear()
