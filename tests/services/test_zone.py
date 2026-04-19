import httpx

from tests.conftest import SUCCESSFUL_RESPONSE


class TestZoneService:
    def test_create(self, client, mock_api):
        route = mock_api.post("/zone").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.zone.create({"origin": "example.com"})
        assert result.status_code == 200
        assert route.called

    def test_info(self, client, mock_api):
        route = mock_api.get("/zone/example.com/ns1.autodns.com").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.zone.info("example.com", "ns1.autodns.com")
        assert result.status_code == 200
        assert route.called

    def test_update(self, client, mock_api):
        route = mock_api.put("/zone/example.com/ns1.autodns.com").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.zone.update("example.com", "ns1.autodns.com", {"soa": {}})
        assert result.status_code == 200
        assert route.called

    def test_delete(self, client, mock_api):
        route = mock_api.delete("/zone/example.com/ns1.autodns.com").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.zone.delete("example.com", "ns1.autodns.com")
        assert result.status_code == 200
        assert route.called

    def test_list(self, client, mock_api):
        route = mock_api.post("/zone/_search").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.zone.list()
        assert result.status_code == 200
        assert route.called

    def test_stream(self, client, mock_api):
        route = mock_api.post("/zone/example.com/_stream").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.zone.stream("example.com", {"adds": [], "rems": []})
        assert result.status_code == 200
        assert route.called

    def test_import_zone(self, client, mock_api):
        route = mock_api.post("/zone/example.com/ns1.autodns.com/_import").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.zone.import_zone(
            "example.com", "ns1.autodns.com", {"origin": "example.com"}
        )
        assert result.status_code == 200
        assert route.called
