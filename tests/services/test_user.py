import httpx

from tests.conftest import SUCCESSFUL_RESPONSE


class TestUserService:
    def test_create(self, client, mock_api):
        route = mock_api.post("/user").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.user.create({"user": "newuser", "context": 4})
        assert result.status_code == 200
        assert route.called

    def test_info(self, client, mock_api):
        route = mock_api.get("/user/testuser/4").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.user.info("testuser", 4)
        assert result.status_code == 200
        assert route.called

    def test_update(self, client, mock_api):
        route = mock_api.put("/user/testuser/4").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.user.update("testuser", 4, {"defaultEmail": "a@b.com"})
        assert result.status_code == 200
        assert route.called

    def test_delete(self, client, mock_api):
        route = mock_api.delete("/user/testuser/4").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.user.delete("testuser", 4)
        assert result.status_code == 200
        assert route.called

    def test_list(self, client, mock_api):
        route = mock_api.post("/user/_search").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.user.list()
        assert result.status_code == 200
        assert route.called
