from __future__ import annotations

from ._base import BaseService


class RedirectService(BaseService):
    def create(self, body: dict, *, headers: dict | None = None):
        return self._request("POST", "/redirect", json=body, headers=headers)

    def info(self, source: str, *, headers: dict | None = None):
        return self._request("GET", f"/redirect/{source}", headers=headers)

    def update(self, source: str, body: dict, *, headers: dict | None = None):
        return self._request(
            "PUT", f"/redirect/{source}", json=body, headers=headers
        )

    def delete(self, source: str, *, headers: dict | None = None):
        return self._request("DELETE", f"/redirect/{source}", headers=headers)

    def list(
        self,
        body: dict | None = None,
        *,
        keys: list[str] | None = None,
        headers: dict | None = None,
    ):
        return self._request(
            "POST",
            "/redirect/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
        )
