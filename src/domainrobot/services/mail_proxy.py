from __future__ import annotations

from ..models.resources import MailProxy
from ._base import BaseService


class MailProxyService(BaseService):
    """Mail proxy operations."""

    def create(self, body: dict, *, headers: dict | None = None):
        """Create a new mail proxy.

        :param body: MailProxy data.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.MailProxy` data.
        """
        return self._request("POST", "/mailProxy", json=body, headers=headers, model=MailProxy)

    def info(self, domain: str, *, headers: dict | None = None):
        """Inquire data for a mail proxy.

        :param domain: Domain name.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.MailProxy` data.
        """
        return self._request("GET", f"/mailProxy/{domain}", headers=headers, model=MailProxy)

    def update(self, domain: str, body: dict, *, headers: dict | None = None):
        """Update a mail proxy.

        :param domain: Domain name.
        :param body: MailProxy data to update.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.MailProxy` data.
        """
        return self._request(
            "PUT", f"/mailProxy/{domain}", json=body, headers=headers, model=MailProxy
        )

    def delete(self, domain: str, *, headers: dict | None = None):
        """Delete a mail proxy.

        :param domain: Domain name.
        :param headers: Optional extra HTTP headers.
        """
        return self._request("DELETE", f"/mailProxy/{domain}", headers=headers)

    def list(
        self,
        body: dict | None = None,
        *,
        keys: list[str] | None = None,
        headers: dict | None = None,
    ):
        """List mail proxies.

        :param body: Optional query filters.
        :param keys: Additional data keys to return.
        :param headers: Optional extra HTTP headers.
        :returns: Response with list of :class:`~domainrobot.models.resources.MailProxy`.
        """
        return self._request(
            "POST",
            "/mailProxy/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
            model=MailProxy,
        )
