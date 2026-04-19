from domainrobot.exceptions import (
    DomainrobotApiError,
    DomainrobotError,
    DomainrobotTransportError,
)


class TestDomainrobotApiError:
    def test_message_from_messages(self):
        exc = DomainrobotApiError(
            status_code=400,
            stid="stid-1",
            messages=[{"text": "Bad request"}, {"text": "Field missing"}],
            response_body={},
        )
        assert str(exc) == "Bad request; Field missing"
        assert exc.status_code == 400
        assert exc.stid == "stid-1"

    def test_message_fallback_when_no_messages(self):
        exc = DomainrobotApiError(
            status_code=500,
            stid=None,
            messages=[],
            response_body={},
        )
        assert str(exc) == "HTTP 500"

    def test_message_from_dict_without_text(self):
        exc = DomainrobotApiError(
            status_code=403,
            stid=None,
            messages=[{"code": "E001"}],
            response_body={},
        )
        assert "E001" in str(exc)

    def test_inherits_from_base(self):
        exc = DomainrobotApiError(400, None, [], {})
        assert isinstance(exc, DomainrobotError)
        assert isinstance(exc, Exception)


class TestDomainrobotTransportError:
    def test_message_and_original(self):
        original = ConnectionError("connection refused")
        exc = DomainrobotTransportError("network error", original=original)
        assert str(exc) == "network error"
        assert exc.original is original

    def test_without_original(self):
        exc = DomainrobotTransportError("timeout")
        assert exc.original is None

    def test_inherits_from_base(self):
        exc = DomainrobotTransportError("err")
        assert isinstance(exc, DomainrobotError)
