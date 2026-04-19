from __future__ import annotations

from ._base import BaseService


class SslContactService(BaseService):
    def create(self, body: dict, *, headers: dict | None = None):
        return self._request("POST", "/sslcontact", json=body, headers=headers)

    def info(self, ssl_contact_id: int, *, headers: dict | None = None):
        return self._request(
            "GET", f"/sslcontact/{ssl_contact_id}", headers=headers
        )

    def update(
        self, ssl_contact_id: int, body: dict, *, headers: dict | None = None
    ):
        return self._request(
            "PUT", f"/sslcontact/{ssl_contact_id}", json=body, headers=headers
        )

    def delete(self, ssl_contact_id: int, *, headers: dict | None = None):
        return self._request(
            "DELETE", f"/sslcontact/{ssl_contact_id}", headers=headers
        )

    def list(
        self,
        body: dict | None = None,
        *,
        keys: list[str] | None = None,
        headers: dict | None = None,
    ):
        return self._request(
            "POST",
            "/sslcontact/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
        )
