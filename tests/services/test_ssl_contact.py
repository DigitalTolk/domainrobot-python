import httpx

from tests.conftest import SUCCESSFUL_RESPONSE


class TestSslContactService:
    def test_create(self, client, mock_api):
        route = mock_api.post("/sslcontact").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.ssl_contact.create({"fname": "John"})
        assert result.status_code == 200
        assert route.called

    def test_info(self, client, mock_api):
        route = mock_api.get("/sslcontact/1").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.ssl_contact.info(1)
        assert result.status_code == 200
        assert route.called

    def test_update(self, client, mock_api):
        route = mock_api.put("/sslcontact/1").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.ssl_contact.update(1, {"fname": "Jane"})
        assert result.status_code == 200
        assert route.called

    def test_delete(self, client, mock_api):
        route = mock_api.delete("/sslcontact/1").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.ssl_contact.delete(1)
        assert result.status_code == 200
        assert route.called

    def test_list(self, client, mock_api):
        route = mock_api.post("/sslcontact/_search").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.ssl_contact.list()
        assert result.status_code == 200
        assert route.called
