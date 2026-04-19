from __future__ import annotations

from ._base import BaseService


class UserService(BaseService):
    def create(self, body: dict, *, headers: dict | None = None):
        return self._request("POST", "/user", json=body, headers=headers)

    def info(self, user: str, context: int, *, headers: dict | None = None):
        return self._request(
            "GET", f"/user/{user}/{context}", headers=headers
        )

    def update(
        self, user: str, context: int, body: dict, *, headers: dict | None = None
    ):
        return self._request(
            "PUT", f"/user/{user}/{context}", json=body, headers=headers
        )

    def delete(self, user: str, context: int, *, headers: dict | None = None):
        return self._request(
            "DELETE", f"/user/{user}/{context}", headers=headers
        )

    def list(self, body: dict | None = None, *, headers: dict | None = None):
        return self._request(
            "POST", "/user/_search", json=body or {}, headers=headers
        )
