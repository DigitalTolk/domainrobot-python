from __future__ import annotations

from ._base import BaseService


class SubscriptionService(BaseService):
    def create(self, body: dict, *, headers: dict | None = None):
        return self._request("POST", "/subscription", json=body, headers=headers)

    def update(
        self, contract_id: int, body: dict, *, headers: dict | None = None
    ):
        return self._request(
            "PUT", f"/subscription/{contract_id}", json=body, headers=headers
        )

    def delete(self, contract_id: int, *, headers: dict | None = None):
        return self._request(
            "DELETE", f"/subscription/{contract_id}", headers=headers
        )

    def list(
        self,
        body: dict | None = None,
        *,
        headers: dict | None = None,
    ):
        return self._request(
            "POST",
            "/subscription/_search",
            json=body or {},
            headers=headers,
        )
