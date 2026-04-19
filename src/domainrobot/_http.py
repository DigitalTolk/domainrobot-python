from __future__ import annotations

from typing import Any

import httpx

from importlib.metadata import version

from .exceptions import DomainrobotApiError, DomainrobotTransportError
from .headers import HEADER_CONTEXT
from .response import DomainrobotResponse

_VERSION = version("domainrobot")


class HttpClient:
    """Low-level HTTP transport wrapping httpx.Client."""

    def __init__(
        self,
        base_url: str,
        username: str,
        password: str,
        context: int | None = None,
        default_headers: dict[str, str] | None = None,
        timeout: float = 30.0,
    ):
        headers: dict[str, str] = {
            "User-Agent": f"domainrobot-python/{_VERSION}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        if context is not None:
            headers[HEADER_CONTEXT] = str(context)
        if default_headers:
            headers.update(default_headers)

        self._client = httpx.Client(
            base_url=base_url,
            auth=(username, password),
            headers=headers,
            timeout=timeout,
        )

    def request(
        self,
        method: str,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> DomainrobotResponse:
        try:
            resp = self._client.request(
                method,
                path,
                json=json,
                params=params,
                headers=headers,
            )
        except httpx.TransportError as exc:
            raise DomainrobotTransportError(str(exc), original=exc) from exc

        body: dict[str, Any] = resp.json() if resp.content else {}

        if resp.is_success:
            return DomainrobotResponse(
                status_code=resp.status_code,
                body=body,
                headers=dict(resp.headers),
            )

        raise DomainrobotApiError(
            status_code=resp.status_code,
            stid=body.get("stid"),
            messages=body.get("messages", []),
            response_body=body,
        )

    def close(self) -> None:
        self._client.close()
