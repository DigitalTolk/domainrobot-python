import pytest
import respx

from domainrobot import Domainrobot

BASE_URL = "https://api.autodns.com/v1"

SUCCESSFUL_RESPONSE = {
    "stid": "20250101-stid",
    "ctid": "ctid-123",
    "status": {"code": "S0001", "text": "OK", "type": "SUCCESS"},
    "data": [{"name": "example.com"}],
    "messages": [{"text": "Operation successful", "code": "S0001", "status": "SUCCESS"}],
}


@pytest.fixture()
def mock_api():
    with respx.mock(base_url=BASE_URL) as rsps:
        yield rsps


@pytest.fixture()
def client():
    c = Domainrobot(
        username="testuser",
        password="testpass",
        context=4,
        base_url=BASE_URL,
    )
    yield c
    c.close()
