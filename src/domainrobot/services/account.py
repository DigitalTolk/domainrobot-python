from __future__ import annotations

from ._base import BaseService


class AccountService(BaseService):
    def info(self, *, headers: dict | None = None):
        return self._request("GET", "/account", headers=headers)

    def update(self, body: dict, *, headers: dict | None = None):
        return self._request("POST", "/account", json=body, headers=headers)
