from __future__ import annotations

from ..models.resources import Account as AccountModel
from ._base import BaseService


class AccountService(BaseService):
    """Customer account operations."""

    def info(self, *, headers: dict | None = None):
        """Inquire account data of the customer.

        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Account` data.
        """
        return self._request("GET", "/account", headers=headers, model=AccountModel)

    def update(self, body: dict, *, headers: dict | None = None):
        """Update the notification parameters.

        :param body: Account data to update.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Account` data.
        """
        return self._request("POST", "/account", json=body, headers=headers, model=AccountModel)
