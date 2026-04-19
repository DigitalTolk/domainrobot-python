import httpx

from tests.conftest import SUCCESSFUL_RESPONSE


class TestTransferOutService:
    def test_list(self, client, mock_api):
        route = mock_api.post("/transferout/_search").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.transfer_out.list()
        assert result.status_code == 200
        assert route.called

    def test_answer(self, client, mock_api):
        route = mock_api.put("/transferout/example.com/ACK").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.transfer_out.answer("example.com", "ACK", {"nackReason": 1})
        assert result.status_code == 200
        assert route.called
