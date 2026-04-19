import httpx

from tests.conftest import SUCCESSFUL_RESPONSE


class TestSubscriptionService:
    def test_create(self, client, mock_api):
        route = mock_api.post("/subscription").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.subscription.create({"articleLabel": "backup_mx"})
        assert result.status_code == 200
        assert route.called

    def test_update(self, client, mock_api):
        route = mock_api.put("/subscription/1").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.subscription.update(1, {"description": "updated"})
        assert result.status_code == 200
        assert route.called

    def test_delete(self, client, mock_api):
        route = mock_api.delete("/subscription/1").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.subscription.delete(1)
        assert result.status_code == 200
        assert route.called

    def test_list(self, client, mock_api):
        route = mock_api.post("/subscription/_search").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.subscription.list()
        assert result.status_code == 200
        assert route.called
