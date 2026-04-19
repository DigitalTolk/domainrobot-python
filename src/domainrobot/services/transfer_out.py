from __future__ import annotations

from ._base import BaseService


class TransferOutService(BaseService):
    def list(
        self,
        body: dict | None = None,
        *,
        keys: list[str] | None = None,
        headers: dict | None = None,
    ):
        return self._request(
            "POST",
            "/transferout/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
        )

    def answer(
        self,
        domain: str,
        answer_type: str,
        body: dict | None = None,
        *,
        headers: dict | None = None,
    ):
        return self._request(
            "PUT",
            f"/transferout/{domain}/{answer_type}",
            json=body,
            headers=headers,
        )
