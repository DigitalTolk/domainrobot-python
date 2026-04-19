import httpx

from tests.conftest import SUCCESSFUL_RESPONSE


class TestHelloService:
    def test_ping(self, client, mock_api):
        route = mock_api.get("/hello").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.hello.ping()
        assert result.status_code == 200
        assert route.called
