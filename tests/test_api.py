from fastapi.testclient import TestClient
from fastapi.responses import Response
from typing import Any

from app.main import app

client: TestClient = TestClient(app)

def test_post_and_get_wallet() -> None:
    address: str = "TGzz8gjYiYRqpfmDwnLxfgPuLVNmpCswVp"
    
    response: Response = client.post("/wallet-info/", json={"address": address})
    assert response.status_code == 200
    
    data: dict[str, Any] = response.json()
    assert "trx_balance" in data
    assert "bandwidth" in data
    assert "energy" in data

    get_response: Response = client.get("/wallet-info/")
    assert get_response.status_code == 200
    result = get_response.json()
    assert isinstance(result, list)
