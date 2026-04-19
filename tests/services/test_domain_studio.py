import httpx

from tests.conftest import SUCCESSFUL_RESPONSE


class TestDomainStudioService:
    def test_search(self, client, mock_api):
        route = mock_api.post("/domainstudio").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.domain_studio.search({"searchToken": "example"})
        assert result.status_code == 200
        assert route.called
        assert b"example" in route.calls[0].request.content
