from __future__ import annotations

from ._base import BaseService


class ContactService(BaseService):
    def create(self, body: dict, *, headers: dict | None = None):
        return self._request("POST", "/contact", json=body, headers=headers)

    def info(self, contact_id: int, *, headers: dict | None = None):
        return self._request("GET", f"/contact/{contact_id}", headers=headers)

    def update(self, contact_id: int, body: dict, *, headers: dict | None = None):
        return self._request(
            "PUT", f"/contact/{contact_id}", json=body, headers=headers
        )

    def delete(self, contact_id: int, *, headers: dict | None = None):
        return self._request("DELETE", f"/contact/{contact_id}", headers=headers)

    def list(
        self,
        body: dict | None = None,
        *,
        keys: list[str] | None = None,
        headers: dict | None = None,
    ):
        return self._request(
            "POST",
            "/contact/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
        )

    def comment_update(
        self, contact_id: int, body: dict, *, headers: dict | None = None
    ):
        return self._request(
            "PUT", f"/contact/{contact_id}/_comment", json=body, headers=headers
        )
