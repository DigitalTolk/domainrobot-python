from __future__ import annotations

from ..models.resources import Domain, DomainCancelation, DomainRestore, Job
from ._base import BaseService


class DomainService(BaseService):
    """Domain operations."""

    def create(self, body: dict, *, headers: dict | None = None):
        """Register a new domain. Async operation.

        :param body: Domain data.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Job` data.
        """
        return self._request("POST", "/domain", json=body, headers=headers, model=Job)

    def info(self, name: str, *, headers: dict | None = None):
        """Inquire data for a domain.

        :param name: Domain name.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Domain` data.
        """
        return self._request("GET", f"/domain/{name}", headers=headers, model=Domain)

    def update(self, name: str, body: dict, *, headers: dict | None = None):
        """Update a domain. Async operation.

        :param name: Domain name.
        :param body: Domain data to update.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Job` data.
        """
        return self._request(
            "PUT", f"/domain/{name}", json=body, headers=headers, model=Job
        )

    def list(
        self,
        body: dict | None = None,
        *,
        keys: list[str] | None = None,
        headers: dict | None = None,
    ):
        """List domains.

        :param body: Optional query filters.
        :param keys: Additional data keys to return.
        :param headers: Optional extra HTTP headers.
        :returns: Response with list of :class:`~domainrobot.models.resources.Domain`.
        """
        return self._request(
            "POST",
            "/domain/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
            model=Domain,
        )

    def transfer(self, body: dict, *, headers: dict | None = None):
        """Transfer a domain. Async operation.

        :param body: Domain transfer data including authinfo.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Job` data.
        """
        return self._request(
            "POST", "/domain/_transfer", json=body, headers=headers, model=Job
        )

    def renew(self, name: str, body: dict, *, headers: dict | None = None):
        """Renew a domain. Async operation.

        :param name: Domain name.
        :param body: Renewal data.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Job` data.
        """
        return self._request(
            "PUT", f"/domain/{name}/_renew", json=body, headers=headers, model=Job
        )

    def restore(self, name: str, body: dict, *, headers: dict | None = None):
        """Restore a domain. Async operation.

        :param name: Domain name.
        :param body: Restore data.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Job` data.
        """
        return self._request(
            "PUT", f"/domain/{name}/_restore", json=body, headers=headers, model=Job
        )

    def restore_list(
        self,
        body: dict | None = None,
        *,
        keys: list[str] | None = None,
        headers: dict | None = None,
    ):
        """List restorable domains.

        :param body: Optional query filters.
        :param keys: Additional data keys to return.
        :param headers: Optional extra HTTP headers.
        :returns: Response with list of :class:`~domainrobot.models.resources.DomainRestore`.
        """
        return self._request(
            "POST",
            "/domain/restore/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
            model=DomainRestore,
        )

    def update_status(self, name: str, body: dict, *, headers: dict | None = None):
        """Update the registry status for a domain. Async operation.

        :param name: Domain name.
        :param body: Status data.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Job` data.
        """
        return self._request(
            "PUT", f"/domain/{name}/_statusUpdate", json=body, headers=headers, model=Job
        )

    def authinfo1_create(self, name: str, *, headers: dict | None = None):
        """Create an AuthInfo1 for a domain.

        :param name: Domain name.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Domain` data.
        """
        return self._request(
            "POST", f"/domain/{name}/_authinfo1", headers=headers, model=Domain
        )

    def authinfo1_delete(self, name: str, *, headers: dict | None = None):
        """Delete an AuthInfo1 for a domain.

        :param name: Domain name.
        :param headers: Optional extra HTTP headers.
        """
        return self._request("DELETE", f"/domain/{name}/_authinfo1", headers=headers)

    def authinfo2_create(self, name: str, *, headers: dict | None = None):
        """Create an AuthInfo2 for a domain.

        :param name: Domain name.
        :param headers: Optional extra HTTP headers.
        """
        return self._request("POST", f"/domain/{name}/_authinfo2", headers=headers)

    def cancelation_create(self, name: str, body: dict, *, headers: dict | None = None):
        """Create a cancelation for a domain.

        :param name: Domain name.
        :param body: Cancelation data.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.DomainCancelation` data.
        """
        return self._request(
            "POST", f"/domain/{name}/cancelation", json=body, headers=headers, model=DomainCancelation
        )

    def cancelation_update(self, name: str, body: dict, *, headers: dict | None = None):
        """Update a cancelation for a domain.

        :param name: Domain name.
        :param body: Cancelation data to update.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.DomainCancelation` data.
        """
        return self._request(
            "PUT", f"/domain/{name}/cancelation", json=body, headers=headers, model=DomainCancelation
        )

    def cancelation_delete(self, name: str, *, headers: dict | None = None):
        """Delete a cancelation for a domain.

        :param name: Domain name.
        :param headers: Optional extra HTTP headers.
        """
        return self._request("DELETE", f"/domain/{name}/cancelation", headers=headers)

    def cancelation_info(self, name: str, *, headers: dict | None = None):
        """Inquire cancelation data for a domain.

        :param name: Domain name.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.DomainCancelation` data.
        """
        return self._request(
            "GET", f"/domain/{name}/cancelation", headers=headers, model=DomainCancelation
        )

    def cancelation_list(
        self,
        body: dict | None = None,
        *,
        keys: list[str] | None = None,
        headers: dict | None = None,
    ):
        """List domain cancelations.

        :param body: Optional query filters.
        :param keys: Additional data keys to return.
        :param headers: Optional extra HTTP headers.
        :returns: Response with list of :class:`~domainrobot.models.resources.DomainCancelation`.
        """
        return self._request(
            "POST",
            "/domain/cancelation/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
            model=DomainCancelation,
        )

    def comment_update(self, name: str, body: dict, *, headers: dict | None = None):
        """Update the comment for a domain.

        :param name: Domain name.
        :param body: Comment data.
        :param headers: Optional extra HTTP headers.
        """
        return self._request("PUT", f"/domain/{name}/_comment", json=body, headers=headers)

    def buy(self, body: dict, *, headers: dict | None = None):
        """Buy a domain from the premium market. Async operation.

        :param body: Domain buy data.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Job` data.
        """
        return self._request("POST", "/domain/_buy", json=body, headers=headers, model=Job)

    def trade(self, body: dict, *, headers: dict | None = None):
        """Change the owner of a domain (trade). Async operation.

        :param body: Domain trade data.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Job` data.
        """
        return self._request("POST", "/domain/_trade", json=body, headers=headers, model=Job)

    def owner_change(self, name: str, body: dict, *, headers: dict | None = None):
        """Change the owner contact of a domain. Async operation.

        :param name: Domain name.
        :param body: Owner change data.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Job` data.
        """
        return self._request(
            "PUT", f"/domain/{name}/_ownerChange", json=body, headers=headers, model=Job
        )

    def dnssec_update(self, name: str, body: dict, *, headers: dict | None = None):
        """Update DNSSEC data for a domain. Async operation.

        :param name: Domain name.
        :param body: DNSSEC data.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Job` data.
        """
        return self._request(
            "PUT", f"/domain/{name}/_dnssec", json=body, headers=headers, model=Job
        )
