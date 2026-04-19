import httpx

from tests.conftest import SUCCESSFUL_RESPONSE


class TestJobService:
    def test_info(self, client, mock_api):
        route = mock_api.get("/job/123").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.job.info(123)
        assert result.status_code == 200
        assert route.called

    def test_list(self, client, mock_api):
        route = mock_api.post("/job/_search").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.job.list()
        assert result.status_code == 200
        assert route.called

    def test_list_with_keys(self, client, mock_api):
        route = mock_api.post("/job/_search").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        client.job.list(keys=["type", "status"])
        request = route.calls[0].request
        url_str = str(request.url)
        assert "keys%5B%5D=type" in url_str
        assert "keys%5B%5D=status" in url_str

    def test_cancel(self, client, mock_api):
        route = mock_api.put("/job/123/_cancel").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.job.cancel(123)
        assert result.status_code == 200
        assert route.called

    def test_confirm(self, client, mock_api):
        route = mock_api.put("/job/123/_confirm").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.job.confirm(123)
        assert result.status_code == 200
        assert route.called
