from __future__ import annotations

from ._base import BaseService


class BackupMxService(BaseService):
    def create(self, body: dict, *, headers: dict | None = None):
        return self._request("POST", "/backupMx", json=body, headers=headers)

    def info(self, domain: str, *, headers: dict | None = None):
        return self._request("GET", f"/backupMx/{domain}", headers=headers)

    def delete(self, domain: str, *, headers: dict | None = None):
        return self._request("DELETE", f"/backupMx/{domain}", headers=headers)

    def list(
        self,
        body: dict | None = None,
        *,
        keys: list[str] | None = None,
        headers: dict | None = None,
    ):
        return self._request(
            "POST",
            "/backupMx/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
        )
