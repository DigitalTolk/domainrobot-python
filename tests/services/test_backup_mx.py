import httpx

from tests.conftest import SUCCESSFUL_RESPONSE


class TestBackupMxService:
    def test_create(self, client, mock_api):
        route = mock_api.post("/backupMx").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.backup_mx.create({"domain": "example.com"})
        assert result.status_code == 200
        assert route.called

    def test_info(self, client, mock_api):
        route = mock_api.get("/backupMx/example.com").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.backup_mx.info("example.com")
        assert result.status_code == 200
        assert route.called

    def test_delete(self, client, mock_api):
        route = mock_api.delete("/backupMx/example.com").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.backup_mx.delete("example.com")
        assert result.status_code == 200
        assert route.called

    def test_list(self, client, mock_api):
        route = mock_api.post("/backupMx/_search").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.backup_mx.list()
        assert result.status_code == 200
        assert route.called
