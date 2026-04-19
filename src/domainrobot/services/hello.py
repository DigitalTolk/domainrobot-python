from __future__ import annotations

from ._base import BaseService


class HelloService(BaseService):
    def ping(self, *, headers: dict | None = None):
        return self._request("GET", "/hello", headers=headers)
