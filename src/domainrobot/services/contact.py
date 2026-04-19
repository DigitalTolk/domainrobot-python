from __future__ import annotations

from ..models.resources import Contact
from ._base import BaseService


class ContactService(BaseService):
    """Domain contact operations."""

    def create(self, body: dict, *, headers: dict | None = None):
        """Create a new domain contact.

        :param body: Contact data.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Contact` data.
        """
        return self._request("POST", "/contact", json=body, headers=headers, model=Contact)

    def info(self, contact_id: int, *, headers: dict | None = None):
        """Inquire data for a domain contact.

        :param contact_id: Contact ID.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Contact` data.
        """
        return self._request("GET", f"/contact/{contact_id}", headers=headers, model=Contact)

    def update(self, contact_id: int, body: dict, *, headers: dict | None = None):
        """Update a domain contact.

        :param contact_id: Contact ID.
        :param body: Contact data to update.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Contact` data.
        """
        return self._request(
            "PUT", f"/contact/{contact_id}", json=body, headers=headers, model=Contact
        )

    def delete(self, contact_id: int, *, headers: dict | None = None):
        """Delete a domain contact.

        :param contact_id: Contact ID.
        :param headers: Optional extra HTTP headers.
        """
        return self._request("DELETE", f"/contact/{contact_id}", headers=headers)

    def list(
        self,
        body: dict | None = None,
        *,
        keys: list[str] | None = None,
        headers: dict | None = None,
    ):
        """List domain contacts.

        :param body: Optional query filters.
        :param keys: Additional data keys to return.
        :param headers: Optional extra HTTP headers.
        :returns: Response with list of :class:`~domainrobot.models.resources.Contact`.
        """
        return self._request(
            "POST",
            "/contact/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
            model=Contact,
        )

    def comment_update(
        self, contact_id: int, body: dict, *, headers: dict | None = None
    ):
        """Update the comment for a contact.

        :param contact_id: Contact ID.
        :param body: Comment data.
        :param headers: Optional extra HTTP headers.
        """
        return self._request(
            "PUT", f"/contact/{contact_id}/_comment", json=body, headers=headers
        )
