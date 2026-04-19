from __future__ import annotations

from ..models.resources import Zone
from ._base import BaseService


class ZoneService(BaseService):
    """DNS zone operations."""

    def create(self, body: dict, *, headers: dict | None = None):
        """Create a zone.

        :param body: Zone data.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Zone` data.
        """
        return self._request("POST", "/zone", json=body, headers=headers, model=Zone)

    def info(self, name: str, virtual_ns: str, *, headers: dict | None = None):
        """Inquire data for a zone.

        :param name: Zone origin.
        :param virtual_ns: Virtual name server.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Zone` data.
        """
        return self._request("GET", f"/zone/{name}/{virtual_ns}", headers=headers, model=Zone)

    def update(self, name: str, virtual_ns: str, body: dict, *, headers: dict | None = None):
        """Update a zone.

        :param name: Zone origin.
        :param virtual_ns: Virtual name server.
        :param body: Zone data to update.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Zone` data.
        """
        return self._request(
            "PUT", f"/zone/{name}/{virtual_ns}", json=body, headers=headers, model=Zone
        )

    def delete(self, name: str, virtual_ns: str, *, headers: dict | None = None):
        """Delete a zone.

        :param name: Zone origin.
        :param virtual_ns: Virtual name server.
        :param headers: Optional extra HTTP headers.
        """
        return self._request("DELETE", f"/zone/{name}/{virtual_ns}", headers=headers)

    def list(
        self,
        body: dict | None = None,
        *,
        keys: list[str] | None = None,
        headers: dict | None = None,
    ):
        """List zones.

        :param body: Optional query filters.
        :param keys: Additional data keys to return.
        :param headers: Optional extra HTTP headers.
        :returns: Response with list of :class:`~domainrobot.models.resources.Zone`.
        """
        return self._request(
            "POST", "/zone/_search", json=body or {}, params=self._keys_params(keys),
            headers=headers, model=Zone,
        )

    def stream(self, name: str, body: dict, *, headers: dict | None = None):
        """Add or remove records for a zone (stream update).

        :param name: Zone origin.
        :param body: Stream data with ``adds`` and ``rems`` lists.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Zone` data.
        """
        return self._request(
            "POST", f"/zone/{name}/_stream", json=body, headers=headers, model=Zone
        )

    def import_zone(self, name: str, virtual_ns: str, body: dict, *, headers: dict | None = None):
        """Import a zone.

        :param name: Zone origin.
        :param virtual_ns: Virtual name server.
        :param body: Zone data to import.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Zone` data.
        """
        return self._request(
            "POST", f"/zone/{name}/{virtual_ns}/_import", json=body, headers=headers, model=Zone
        )
