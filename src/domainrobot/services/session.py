from __future__ import annotations

from ..models.resources import User
from ._base import BaseService


class SessionService(BaseService):
    """Session / login operations."""

    def login(self, body: dict, *, headers: dict | None = None):
        """Log in and create a new session.

        :param body: Login credentials.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.User` data.
        """
        return self._request("POST", "/login", json=body, headers=headers, model=User)

    def logout(self, *, headers: dict | None = None):
        """Log out and delete the current session.

        :param headers: Optional extra HTTP headers.
        """
        return self._request("DELETE", "/logout", headers=headers)
