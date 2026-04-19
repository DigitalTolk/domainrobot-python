import httpx
import pytest

from domainrobot.exceptions import DomainrobotApiError
from tests.conftest import SUCCESSFUL_RESPONSE


class TestContactService:
    def test_create(self, client, mock_api):
        route = mock_api.post("/contact").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.contact.create({"type": "PERSON", "fname": "John"})
        assert result.status_code == 200
        assert route.called

    def test_info(self, client, mock_api):
        route = mock_api.get("/contact/1").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.contact.info(1)
        assert result.status_code == 200
        assert route.called

    def test_update(self, client, mock_api):
        route = mock_api.put("/contact/1").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.contact.update(1, {"fname": "Jane"})
        assert result.status_code == 200
        assert route.called

    def test_delete(self, client, mock_api):
        route = mock_api.delete("/contact/1").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.contact.delete(1)
        assert result.status_code == 200
        assert route.called

    def test_list(self, client, mock_api):
        route = mock_api.post("/contact/_search").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.contact.list()
        assert result.status_code == 200
        assert route.called

    def test_list_with_keys(self, client, mock_api):
        route = mock_api.post("/contact/_search").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        client.contact.list(keys=["email", "fname"])
        request = route.calls[0].request
        url_str = str(request.url)
        assert "keys%5B%5D=email" in url_str
        assert "keys%5B%5D=fname" in url_str

    def test_comment_update(self, client, mock_api):
        route = mock_api.put("/contact/1/_comment").mock(
            return_value=httpx.Response(200, json=SUCCESSFUL_RESPONSE)
        )
        result = client.contact.comment_update(1, {"comment": "test"})
        assert result.status_code == 200
        assert route.called

    def test_api_error(self, client, mock_api):
        error_body = {
            "stid": "stid-err",
            "messages": [{"text": "Contact not found"}],
        }
        mock_api.get("/contact/999").mock(
            return_value=httpx.Response(404, json=error_body)
        )
        with pytest.raises(DomainrobotApiError) as exc_info:
            client.contact.info(999)
        assert exc_info.value.status_code == 404
