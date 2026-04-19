from __future__ import annotations

from ..models.resources import SslContact
from ._base import BaseService


class SslContactService(BaseService):
    """SSL contact operations."""

    def create(self, body: dict, *, headers: dict | None = None):
        """Create a new SSL contact.

        :param body: SSL contact data.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.SslContact` data.
        """
        return self._request("POST", "/sslcontact", json=body, headers=headers, model=SslContact)

    def info(self, ssl_contact_id: int, *, headers: dict | None = None):
        """Inquire data for an SSL contact.

        :param ssl_contact_id: SSL contact ID.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.SslContact` data.
        """
        return self._request(
            "GET", f"/sslcontact/{ssl_contact_id}", headers=headers, model=SslContact
        )

    def update(self, ssl_contact_id: int, body: dict, *, headers: dict | None = None):
        """Update an SSL contact.

        :param ssl_contact_id: SSL contact ID.
        :param body: SSL contact data to update.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.SslContact` data.
        """
        return self._request(
            "PUT", f"/sslcontact/{ssl_contact_id}", json=body, headers=headers, model=SslContact
        )

    def delete(self, ssl_contact_id: int, *, headers: dict | None = None):
        """Delete an SSL contact.

        :param ssl_contact_id: SSL contact ID.
        :param headers: Optional extra HTTP headers.
        """
        return self._request("DELETE", f"/sslcontact/{ssl_contact_id}", headers=headers)

    def list(
        self,
        body: dict | None = None,
        *,
        keys: list[str] | None = None,
        headers: dict | None = None,
    ):
        """List SSL contacts.

        :param body: Optional query filters.
        :param keys: Additional data keys to return.
        :param headers: Optional extra HTTP headers.
        :returns: Response with list of :class:`~domainrobot.models.resources.SslContact`.
        """
        return self._request(
            "POST",
            "/sslcontact/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
            model=SslContact,
        )
