from __future__ import annotations

from ..models.resources import PollMessage
from ._base import BaseService


class PollService(BaseService):
    """Poll message operations."""

    def info(self, *, headers: dict | None = None):
        """Inquire the latest poll message.

        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.PollMessage` data.
        """
        return self._request("GET", "/poll", headers=headers, model=PollMessage)

    def confirm(self, poll_id: int, *, headers: dict | None = None):
        """Confirm a poll message.

        :param poll_id: Poll message ID.
        :param headers: Optional extra HTTP headers.
        """
        return self._request("PUT", f"/poll/{poll_id}", headers=headers)
