from __future__ import annotations

from typing import Any


class DomainrobotResponse:
    """Thin wrapper around a successful API response."""

    __slots__ = ("status_code", "stid", "ctid", "status", "data", "messages", "headers")

    def __init__(
        self, status_code: int, body: dict[str, Any], headers: dict[str, str]
    ):
        self.status_code = status_code
        self.stid: str | None = body.get("stid")
        self.ctid: str | None = body.get("ctid")
        self.status: dict | None = body.get("status")
        self.data: list[dict] | None = body.get("data")
        self.messages: list[dict] | None = body.get("messages")
        self.headers = headers

    def __repr__(self) -> str:
        return (
            f"DomainrobotResponse(status_code={self.status_code}, stid={self.stid!r})"
        )
