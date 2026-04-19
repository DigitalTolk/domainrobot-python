import httpx

from tests.conftest import SUCCESSFUL_RESPONSE


class TestRedirectService:
    def test_create(self, client, mock_api):
        route = mock_api.post("/redirect").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.redirect.create({"source": "www.example.com", "target": "example.com"})
        assert result.status_code == 200
        assert route.called

    def test_info(self, client, mock_api):
        route = mock_api.get("/redirect/www.example.com").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.redirect.info("www.example.com")
        assert result.status_code == 200
        assert route.called

    def test_update(self, client, mock_api):
        route = mock_api.put("/redirect/www.example.com").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.redirect.update("www.example.com", {"target": "new.example.com"})
        assert result.status_code == 200
        assert route.called

    def test_delete(self, client, mock_api):
        route = mock_api.delete("/redirect/www.example.com").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.redirect.delete("www.example.com")
        assert result.status_code == 200
        assert route.called

    def test_list(self, client, mock_api):
        route = mock_api.post("/redirect/_search").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.redirect.list()
        assert result.status_code == 200
        assert route.called
