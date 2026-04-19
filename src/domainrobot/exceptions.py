from __future__ import annotations


class DomainrobotError(Exception):
    """Base exception for all domainrobot errors."""


class DomainrobotApiError(DomainrobotError):
    """Raised when the API returns a non-2xx response."""

    def __init__(
        self,
        status_code: int,
        stid: str | None,
        messages: list[dict],
        response_body: dict,
    ):
        #: HTTP status code.
        self.status_code = status_code
        #: Server transaction ID.
        self.stid = stid
        #: Error messages from the API.
        self.messages = messages
        #: Full response body dict.
        self.response_body = response_body
        msg_texts = (
            [m.get("text", str(m)) for m in messages]
            if messages
            else [f"HTTP {status_code}"]
        )
        super().__init__("; ".join(msg_texts))


class DomainrobotTransportError(DomainrobotError):
    """Raised for network/connection errors."""

    def __init__(self, message: str, original: Exception | None = None):
        #: The underlying transport exception, if available.
        self.original = original
        super().__init__(message)
