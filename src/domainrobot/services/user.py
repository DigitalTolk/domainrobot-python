from __future__ import annotations

from ..models.resources import User
from ._base import BaseService


class UserService(BaseService):
    """User management operations."""

    def create(self, body: dict, *, headers: dict | None = None):
        """Create a new user.

        :param body: User data.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.User` data.
        """
        return self._request("POST", "/user", json=body, headers=headers, model=User)

    def info(self, user: str, context: int, *, headers: dict | None = None):
        """Inquire data for a user.

        :param user: Username.
        :param context: Context number.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.User` data.
        """
        return self._request("GET", f"/user/{user}/{context}", headers=headers, model=User)

    def update(self, user: str, context: int, body: dict, *, headers: dict | None = None):
        """Update a user.

        :param user: Username.
        :param context: Context number.
        :param body: User data to update.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.User` data.
        """
        return self._request(
            "PUT", f"/user/{user}/{context}", json=body, headers=headers, model=User
        )

    def delete(self, user: str, context: int, *, headers: dict | None = None):
        """Delete a user.

        :param user: Username.
        :param context: Context number.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.User` data.
        """
        return self._request("DELETE", f"/user/{user}/{context}", headers=headers, model=User)

    def list(self, body: dict | None = None, *, headers: dict | None = None):
        """List users.

        :param body: Optional query filters.
        :param headers: Optional extra HTTP headers.
        :returns: Response with list of :class:`~domainrobot.models.resources.User`.
        """
        return self._request("POST", "/user/_search", json=body or {}, headers=headers, model=User)
