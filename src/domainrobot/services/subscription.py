from __future__ import annotations

from ..models.resources import Subscription
from ._base import BaseService


class SubscriptionService(BaseService):
    """Subscription contract operations."""

    def create(self, body: dict, *, headers: dict | None = None):
        """Create a new subscription.

        :param body: Subscription data.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Subscription` data.
        """
        return self._request("POST", "/subscription", json=body, headers=headers, model=Subscription)

    def update(self, contract_id: int, body: dict, *, headers: dict | None = None):
        """Update a subscription.

        :param contract_id: Contract ID.
        :param body: Subscription data to update.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Subscription` data.
        """
        return self._request(
            "PUT", f"/subscription/{contract_id}", json=body, headers=headers, model=Subscription
        )

    def delete(self, contract_id: int, *, headers: dict | None = None):
        """Delete a subscription.

        :param contract_id: Contract ID.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Subscription` data.
        """
        return self._request(
            "DELETE", f"/subscription/{contract_id}", headers=headers, model=Subscription
        )

    def list(self, body: dict | None = None, *, headers: dict | None = None):
        """List subscriptions.

        :param body: Optional query filters.
        :param headers: Optional extra HTTP headers.
        :returns: Response with list of :class:`~domainrobot.models.resources.Subscription`.
        """
        return self._request(
            "POST", "/subscription/_search", json=body or {}, headers=headers, model=Subscription
        )
