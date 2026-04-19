import httpx

from tests.conftest import SUCCESSFUL_RESPONSE


class TestDomainService:
    def test_create(self, client, mock_api):
        route = mock_api.post("/domain").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain.create({"name": "example.com"})
        assert result.status_code == 200
        assert route.called

    def test_info(self, client, mock_api):
        route = mock_api.get("/domain/example.com").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain.info("example.com")
        assert result.status_code == 200
        assert result.data == [{"name": "example.com"}]
        assert route.called

    def test_update(self, client, mock_api):
        route = mock_api.put("/domain/example.com").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain.update("example.com", {"nameServers": []})
        assert result.status_code == 200
        assert route.called

    def test_list(self, client, mock_api):
        route = mock_api.post("/domain/_search").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain.list()
        assert result.status_code == 200
        assert route.called

    def test_list_with_body_and_keys(self, client, mock_api):
        route = mock_api.post("/domain/_search").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        client.domain.list(
            {"filters": [{"key": "name", "value": "*.com"}]},
            keys=["expire", "status"],
        )
        request = route.calls[0].request
        url_str = str(request.url)
        assert "keys%5B%5D=expire" in url_str
        assert "keys%5B%5D=status" in url_str

    def test_transfer(self, client, mock_api):
        route = mock_api.post("/domain/_transfer").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain.transfer({"name": "example.com", "authinfo": "abc"})
        assert result.status_code == 200
        assert route.called

    def test_renew(self, client, mock_api):
        route = mock_api.put("/domain/example.com/_renew").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain.renew("example.com", {"period": {"unit": "YEAR", "period": 1}})
        assert result.status_code == 200
        assert route.called

    def test_restore(self, client, mock_api):
        route = mock_api.put("/domain/example.com/_restore").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain.restore("example.com", {})
        assert result.status_code == 200
        assert route.called

    def test_restore_list(self, client, mock_api):
        route = mock_api.post("/domain/restore/_search").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain.restore_list()
        assert result.status_code == 200
        assert route.called

    def test_update_status(self, client, mock_api):
        route = mock_api.put("/domain/example.com/_statusUpdate").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain.update_status("example.com", {"registryStatus": "LOCK"})
        assert result.status_code == 200
        assert route.called

    def test_authinfo1_create(self, client, mock_api):
        route = mock_api.post("/domain/example.com/_authinfo1").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain.authinfo1_create("example.com")
        assert result.status_code == 200
        assert route.called

    def test_authinfo1_delete(self, client, mock_api):
        route = mock_api.delete("/domain/example.com/_authinfo1").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain.authinfo1_delete("example.com")
        assert result.status_code == 200
        assert route.called

    def test_authinfo2_create(self, client, mock_api):
        route = mock_api.post("/domain/example.com/_authinfo2").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain.authinfo2_create("example.com")
        assert result.status_code == 200
        assert route.called

    def test_cancelation_create(self, client, mock_api):
        route = mock_api.post("/domain/example.com/cancelation").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain.cancelation_create("example.com", {"type": "DELETE"})
        assert result.status_code == 200
        assert route.called

    def test_cancelation_update(self, client, mock_api):
        route = mock_api.put("/domain/example.com/cancelation").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain.cancelation_update("example.com", {"type": "DELETE"})
        assert result.status_code == 200
        assert route.called

    def test_cancelation_delete(self, client, mock_api):
        route = mock_api.delete("/domain/example.com/cancelation").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain.cancelation_delete("example.com")
        assert result.status_code == 200
        assert route.called

    def test_cancelation_info(self, client, mock_api):
        route = mock_api.get("/domain/example.com/cancelation").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain.cancelation_info("example.com")
        assert result.status_code == 200
        assert route.called

    def test_cancelation_list(self, client, mock_api):
        route = mock_api.post("/domain/cancelation/_search").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain.cancelation_list()
        assert result.status_code == 200
        assert route.called

    def test_comment_update(self, client, mock_api):
        route = mock_api.put("/domain/example.com/_comment").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain.comment_update("example.com", {"comment": "test"})
        assert result.status_code == 200
        assert route.called

    def test_buy(self, client, mock_api):
        route = mock_api.post("/domain/_buy").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain.buy({"name": "example.com"})
        assert result.status_code == 200
        assert route.called

    def test_trade(self, client, mock_api):
        route = mock_api.post("/domain/_trade").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain.trade({"name": "example.com"})
        assert result.status_code == 200
        assert route.called

    def test_owner_change(self, client, mock_api):
        route = mock_api.put("/domain/example.com/_ownerChange").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain.owner_change("example.com", {"ownerc": {}})
        assert result.status_code == 200
        assert route.called

    def test_dnssec_update(self, client, mock_api):
        route = mock_api.put("/domain/example.com/_dnssec").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain.dnssec_update("example.com", {"dnssecData": []})
        assert result.status_code == 200
        assert route.called

    def test_custom_headers_forwarded(self, client, mock_api):
        route = mock_api.get("/domain/example.com").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        client.domain.info("example.com", headers={"X-Domainrobot-Demo": "true"})
        request = route.calls[0].request
        assert request.headers["x-domainrobot-demo"] == "true"
