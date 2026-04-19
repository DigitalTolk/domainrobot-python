from __future__ import annotations

from ..models.resources import Redirect
from ._base import BaseService


class RedirectService(BaseService):
    """Domain and email redirect operations."""

    def create(self, body: dict, *, headers: dict | None = None):
        """Create a new redirect.

        :param body: Redirect data.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Redirect` data.
        """
        return self._request("POST", "/redirect", json=body, headers=headers, model=Redirect)

    def info(self, source: str, *, headers: dict | None = None):
        """Inquire data for a redirect.

        :param source: Source domain.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Redirect` data.
        """
        return self._request("GET", f"/redirect/{source}", headers=headers, model=Redirect)

    def update(self, source: str, body: dict, *, headers: dict | None = None):
        """Update a redirect.

        :param source: Source domain.
        :param body: Redirect data to update.
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.Redirect` data.
        """
        return self._request(
            "PUT", f"/redirect/{source}", json=body, headers=headers, model=Redirect
        )

    def delete(self, source: str, *, headers: dict | None = None):
        """Delete a redirect.

        :param source: Source domain.
        :param headers: Optional extra HTTP headers.
        """
        return self._request("DELETE", f"/redirect/{source}", headers=headers)

    def list(
        self,
        body: dict | None = None,
        *,
        keys: list[str] | None = None,
        headers: dict | None = None,
    ):
        """List redirects.

        :param body: Optional query filters.
        :param keys: Additional data keys to return.
        :param headers: Optional extra HTTP headers.
        :returns: Response with list of :class:`~domainrobot.models.resources.Redirect`.
        """
        return self._request(
            "POST",
            "/redirect/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
            model=Redirect,
        )
