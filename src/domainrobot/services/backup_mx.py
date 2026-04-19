from __future__ import annotations

from ..models.resources import BackupMx
from ._base import BaseService


class BackupMxService(BaseService):
    """BackupMX record operations."""

    def create(self, body: dict, *, headers: dict | None = None):
        """Create a new BackupMX.

        :param body: BackupMX data.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.BackupMx` data.
        """
        return self._request("POST", "/backupMx", json=body, headers=headers, model=BackupMx)

    def info(self, domain: str, *, headers: dict | None = None):
        """Inquire data for a BackupMX.

        :param domain: Domain name.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.BackupMx` data.
        """
        return self._request("GET", f"/backupMx/{domain}", headers=headers, model=BackupMx)

    def delete(self, domain: str, *, headers: dict | None = None):
        """Delete a BackupMX.

        :param domain: Domain name.
        :param headers: Optional extra HTTP headers.
        """
        return self._request("DELETE", f"/backupMx/{domain}", headers=headers)

    def list(
        self,
        body: dict | None = None,
        *,
        keys: list[str] | None = None,
        headers: dict | None = None,
    ):
        """List BackupMX entries.

        :param body: Optional query filters.
        :param keys: Additional data keys to return.
        :param headers: Optional extra HTTP headers.
        :returns: Response with list of :class:`~domainrobot.models.resources.BackupMx`.
        """
        return self._request(
            "POST",
            "/backupMx/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
            model=BackupMx,
        )
