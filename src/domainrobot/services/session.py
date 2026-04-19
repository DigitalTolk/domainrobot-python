from __future__ import annotations

from ._base import BaseService


class SessionService(BaseService):
    def login(self, body: dict, *, headers: dict | None = None):
        return self._request("POST", "/login", json=body, headers=headers)

    def logout(self, *, headers: dict | None = None):
        return self._request("DELETE", "/logout", headers=headers)
