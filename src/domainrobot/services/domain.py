from __future__ import annotations

from ._base import BaseService


class DomainService(BaseService):
    def create(self, body: dict, *, headers: dict | None = None):
        return self._request("POST", "/domain", json=body, headers=headers)

    def info(self, name: str, *, headers: dict | None = None):
        return self._request("GET", f"/domain/{name}", headers=headers)

    def update(self, name: str, body: dict, *, headers: dict | None = None):
        return self._request(
            "PUT", f"/domain/{name}", json=body, headers=headers
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
            "/domain/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
        )

    def transfer(self, body: dict, *, headers: dict | None = None):
        return self._request(
            "POST", "/domain/_transfer", json=body, headers=headers
        )

    def renew(self, name: str, body: dict, *, headers: dict | None = None):
        return self._request(
            "PUT", f"/domain/{name}/_renew", json=body, headers=headers
        )

    def restore(self, name: str, body: dict, *, headers: dict | None = None):
        return self._request(
            "PUT", f"/domain/{name}/_restore", json=body, headers=headers
        )

    def restore_list(
        self,
        body: dict | None = None,
        *,
        keys: list[str] | None = None,
        headers: dict | None = None,
    ):
        return self._request(
            "POST",
            "/domain/restore/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
        )

    def update_status(
        self, name: str, body: dict, *, headers: dict | None = None
    ):
        return self._request(
            "PUT", f"/domain/{name}/_statusUpdate", json=body, headers=headers
        )

    def authinfo1_create(self, name: str, *, headers: dict | None = None):
        return self._request(
            "POST", f"/domain/{name}/_authinfo1", headers=headers
        )

    def authinfo1_delete(self, name: str, *, headers: dict | None = None):
        return self._request(
            "DELETE", f"/domain/{name}/_authinfo1", headers=headers
        )

    def authinfo2_create(self, name: str, *, headers: dict | None = None):
        return self._request(
            "POST", f"/domain/{name}/_authinfo2", headers=headers
        )

    def cancelation_create(
        self, name: str, body: dict, *, headers: dict | None = None
    ):
        return self._request(
            "POST", f"/domain/{name}/cancelation", json=body, headers=headers
        )

    def cancelation_update(
        self, name: str, body: dict, *, headers: dict | None = None
    ):
        return self._request(
            "PUT", f"/domain/{name}/cancelation", json=body, headers=headers
        )

    def cancelation_delete(self, name: str, *, headers: dict | None = None):
        return self._request(
            "DELETE", f"/domain/{name}/cancelation", headers=headers
        )

    def cancelation_info(self, name: str, *, headers: dict | None = None):
        return self._request(
            "GET", f"/domain/{name}/cancelation", headers=headers
        )

    def cancelation_list(
        self,
        body: dict | None = None,
        *,
        keys: list[str] | None = None,
        headers: dict | None = None,
    ):
        return self._request(
            "POST",
            "/domain/cancelation/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
        )

    def comment_update(
        self, name: str, body: dict, *, headers: dict | None = None
    ):
        return self._request(
            "PUT", f"/domain/{name}/_comment", json=body, headers=headers
        )

    def buy(self, body: dict, *, headers: dict | None = None):
        return self._request("POST", "/domain/_buy", json=body, headers=headers)

    def trade(self, body: dict, *, headers: dict | None = None):
        return self._request(
            "POST", "/domain/_trade", json=body, headers=headers
        )

    def owner_change(
        self, name: str, body: dict, *, headers: dict | None = None
    ):
        return self._request(
            "PUT", f"/domain/{name}/_ownerChange", json=body, headers=headers
        )

    def dnssec_update(
        self, name: str, body: dict, *, headers: dict | None = None
    ):
        return self._request(
            "PUT", f"/domain/{name}/_dnssec", json=body, headers=headers
        )
