from __future__ import annotations

from ._base import BaseService


class MailProxyService(BaseService):
    def create(self, body: dict, *, headers: dict | None = None):
        return self._request("POST", "/mailProxy", json=body, headers=headers)

    def info(self, domain: str, *, headers: dict | None = None):
        return self._request("GET", f"/mailProxy/{domain}", headers=headers)

    def update(self, domain: str, body: dict, *, headers: dict | None = None):
        return self._request(
            "PUT", f"/mailProxy/{domain}", json=body, headers=headers
        )

    def delete(self, domain: str, *, headers: dict | None = None):
        return self._request("DELETE", f"/mailProxy/{domain}", headers=headers)

    def list(
        self,
        body: dict | None = None,
        *,
        keys: list[str] | None = None,
        headers: dict | None = None,
    ):
        return self._request(
            "POST",
            "/mailProxy/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
        )
