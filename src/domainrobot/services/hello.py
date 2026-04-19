from __future__ import annotations

from ._base import BaseService


class HelloService(BaseService):
    """Connection test operations."""

    def ping(self, *, headers: dict | None = None):
        """Test the connection to the API.

        :param headers: Optional extra HTTP headers.
        """
        return self._request("GET", "/hello", headers=headers)
