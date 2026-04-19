import httpx

from tests.conftest import SUCCESSFUL_RESPONSE


class TestMailProxyService:
    def test_create(self, client, mock_api):
        route = mock_api.post("/mailProxy").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.mail_proxy.create({"domain": "example.com"})
        assert result.status_code == 200
        assert route.called

    def test_info(self, client, mock_api):
        route = mock_api.get("/mailProxy/example.com").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.mail_proxy.info("example.com")
        assert result.status_code == 200
        assert route.called

    def test_update(self, client, mock_api):
        route = mock_api.put("/mailProxy/example.com").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.mail_proxy.update("example.com", {"target": "mail.example.com"})
        assert result.status_code == 200
        assert route.called

    def test_delete(self, client, mock_api):
        route = mock_api.delete("/mailProxy/example.com").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.mail_proxy.delete("example.com")
        assert result.status_code == 200
        assert route.called

    def test_list(self, client, mock_api):
        route = mock_api.post("/mailProxy/_search").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.mail_proxy.list()
        assert result.status_code == 200
        assert route.called
