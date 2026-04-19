from __future__ import annotations

from ._base import BaseService


class JobService(BaseService):
    def info(self, job_id: int, *, headers: dict | None = None):
        return self._request("GET", f"/job/{job_id}", headers=headers)

    def list(
        self,
        body: dict | None = None,
        *,
        keys: list[str] | None = None,
        headers: dict | None = None,
    ):
        return self._request(
            "POST",
            "/job/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
        )

    def cancel(self, job_id: int, *, headers: dict | None = None):
        return self._request("PUT", f"/job/{job_id}/_cancel", headers=headers)

    def confirm(self, job_id: int, *, headers: dict | None = None):
        return self._request("PUT", f"/job/{job_id}/_confirm", headers=headers)
