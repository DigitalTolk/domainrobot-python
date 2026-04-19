import httpx
import pytest

from domainrobot._http import HttpClient
from domainrobot.exceptions import DomainrobotApiError, DomainrobotTransportError
from domainrobot.response import DomainrobotResponse
from tests.conftest import BASE_URL

OK_BODY = {
    "stid": "stid-1",
    "status": {"code": "S0001", "text": "OK", "type": "SUCCESS"},
    "data": [],
}


@pytest.fixture()
def http():
    c = HttpClient(
        base_url=BASE_URL,
        username="user",
        password="pass",
        context=4,
    )
    yield c
    c.close()


class TestHttpClientRequest:
    def test_success_returns_response(self, http, mock_api):
        mock_api.get("/hello").mock(return_value=httpx.Response(200, json=OK_BODY))
        result = http.request("GET", "/hello")
        assert isinstance(result, DomainrobotResponse)
        assert result.status_code == 200
        assert result.stid == "stid-1"

    def test_sends_basic_auth(self, http, mock_api):
        route = mock_api.get("/hello").mock(
            return_value=httpx.Response(200, json=OK_BODY)
        )
        http.request("GET", "/hello")
        request = route.calls[0].request
        assert request.headers["authorization"].startswith("Basic ")

    def test_sends_context_header(self, http, mock_api):
        route = mock_api.get("/hello").mock(
            return_value=httpx.Response(200, json=OK_BODY)
        )
        http.request("GET", "/hello")
        request = route.calls[0].request
        assert request.headers["x-domainrobot-context"] == "4"

    def test_sends_json_body(self, http, mock_api):
        route = mock_api.post("/domain/_search").mock(
            return_value=httpx.Response(200, json=OK_BODY)
        )
        http.request("POST", "/domain/_search", json={"filters": []})
        request = route.calls[0].request
        assert b'"filters"' in request.content

    def test_sends_query_params(self, http, mock_api):
        route = mock_api.post("/domain/_search").mock(
            return_value=httpx.Response(200, json=OK_BODY)
        )
        http.request("POST", "/domain/_search", params={"keys[]": ["expire"]})
        request = route.calls[0].request
        assert "keys%5B%5D=expire" in str(request.url)

    def test_sends_extra_headers(self, http, mock_api):
        route = mock_api.get("/hello").mock(
            return_value=httpx.Response(200, json=OK_BODY)
        )
        http.request("GET", "/hello", headers={"X-Domainrobot-Demo": "true"})
        request = route.calls[0].request
        assert request.headers["x-domainrobot-demo"] == "true"

    def test_api_error_raises(self, http, mock_api):
        error_body = {
            "stid": "stid-err",
            "messages": [{"text": "Not found", "code": "E0001"}],
        }
        mock_api.get("/domain/missing.com").mock(
            return_value=httpx.Response(404, json=error_body)
        )
        with pytest.raises(DomainrobotApiError) as exc_info:
            http.request("GET", "/domain/missing.com")
        assert exc_info.value.status_code == 404
        assert exc_info.value.stid == "stid-err"
        assert "Not found" in str(exc_info.value)

    def test_transport_error_raises(self, http, mock_api):
        mock_api.get("/hello").mock(side_effect=httpx.ConnectError("refused"))
        with pytest.raises(DomainrobotTransportError) as exc_info:
            http.request("GET", "/hello")
        assert "refused" in str(exc_info.value)
        assert isinstance(exc_info.value.original, httpx.ConnectError)

    def test_empty_response_body(self, http, mock_api):
        mock_api.delete("/contact/1").mock(
            return_value=httpx.Response(200, content=b"")
        )
        result = http.request("DELETE", "/contact/1")
        assert result.status_code == 200
        assert result.data is None


class TestHttpClientInit:
    def test_default_headers_applied(self):
        c = HttpClient(
            base_url=BASE_URL,
            username="u",
            password="p",
            default_headers={"X-Custom": "val"},
        )
        assert c._client.headers["x-custom"] == "val"
        c.close()

    def test_no_context_header_when_none(self):
        c = HttpClient(base_url=BASE_URL, username="u", password="p")
        assert "x-domainrobot-context" not in c._client.headers
        c.close()
