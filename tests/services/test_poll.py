import httpx

from tests.conftest import SUCCESSFUL_RESPONSE


class TestPollService:
    def test_info(self, client, mock_api):
        route = mock_api.get("/poll").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.poll.info()
        assert result.status_code == 200
        assert route.called

    def test_confirm(self, client, mock_api):
        route = mock_api.put("/poll/42").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.poll.confirm(42)
        assert result.status_code == 200
        assert route.called
