from __future__ import annotations

from ..models.resources import DomainEnvelope
from ._base import BaseService


class DomainStudioService(BaseService):
    """DomainStudio search operations."""

    def search(self, body: dict, *, headers: dict | None = None):
        """Search for free, premium, and alternate domain names.

        :param body: Search request data.
        :param headers: Optional extra HTTP headers.
        :returns: Response with list of :class:`~domainrobot.models.resources.DomainEnvelope`.
        """
        return self._request("POST", "/domainstudio", json=body, headers=headers, model=DomainEnvelope)
