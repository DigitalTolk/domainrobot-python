from __future__ import annotations

from ._base import BaseService


class ZoneService(BaseService):
    def create(self, body: dict, *, headers: dict | None = None):
        return self._request("POST", "/zone", json=body, headers=headers)

    def info(
        self, name: str, virtual_ns: str, *, headers: dict | None = None
    ):
        return self._request(
            "GET", f"/zone/{name}/{virtual_ns}", headers=headers
        )

    def update(
        self, name: str, virtual_ns: str, body: dict, *, headers: dict | None = None
    ):
        return self._request(
            "PUT", f"/zone/{name}/{virtual_ns}", json=body, headers=headers
        )

    def delete(
        self, name: str, virtual_ns: str, *, headers: dict | None = None
    ):
        return self._request(
            "DELETE", f"/zone/{name}/{virtual_ns}", headers=headers
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
            "/zone/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
        )

    def stream(self, name: str, body: dict, *, headers: dict | None = None):
        return self._request(
            "POST", f"/zone/{name}/_stream", json=body, headers=headers
        )

    def import_zone(
        self, name: str, virtual_ns: str, body: dict, *, headers: dict | None = None
    ):
        return self._request(
            "POST",
            f"/zone/{name}/{virtual_ns}/_import",
            json=body,
            headers=headers,
        )
