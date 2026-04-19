import httpx

from tests.conftest import SUCCESSFUL_RESPONSE


class TestAccountService:
    def test_info(self, client, mock_api):
        route = mock_api.get("/account").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.account.info()
        assert result.status_code == 200
        assert route.called

    def test_update(self, client, mock_api):
        route = mock_api.post("/account").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.account.update({"minRunningTotalNotification": 100})
        assert result.status_code == 200
        assert route.called
