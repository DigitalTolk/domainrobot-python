from __future__ import annotations

from ..models.resources import ObjectJob
from ._base import BaseService


class JobService(BaseService):
    """Asynchronous job operations."""

    def info(self, job_id: int, *, headers: dict | None = None):
        """Inquire data for a job.

        :param job_id: Job ID.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.ObjectJob` data.
        """
        return self._request("GET", f"/job/{job_id}", headers=headers, model=ObjectJob)

    def list(
        self,
        body: dict | None = None,
        *,
        keys: list[str] | None = None,
        headers: dict | None = None,
    ):
        """List jobs.

        :param body: Optional query filters.
        :param keys: Additional data keys to return.
        :param headers: Optional extra HTTP headers.
        :returns: Response with list of :class:`~domainrobot.models.resources.ObjectJob`.
        """
        return self._request(
            "POST",
            "/job/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
            model=ObjectJob,
        )

    def cancel(self, job_id: int, *, headers: dict | None = None):
        """Cancel a job.

        :param job_id: Job ID.
        :param headers: Optional extra HTTP headers.
        """
        return self._request("PUT", f"/job/{job_id}/_cancel", headers=headers)

    def confirm(self, job_id: int, *, headers: dict | None = None):
        """Confirm a job.

        :param job_id: Job ID.
        :param headers: Optional extra HTTP headers.
        """
        return self._request("PUT", f"/job/{job_id}/_confirm", headers=headers)
