import httpx

from tests.conftest import SUCCESSFUL_RESPONSE


class TestSessionService:
    def test_login(self, client, mock_api):
        route = mock_api.post("/login").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.session.login({"user": "admin", "password": "secret", "context": 4})
        assert result.status_code == 200
        assert route.called

    def test_logout(self, client, mock_api):
        route = mock_api.delete("/logout").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.session.logout()
        assert result.status_code == 200
        assert route.called
