from __future__ import annotations

from typing import Literal

from ..models.resources import TransferOut
from ._base import BaseService


class TransferOutService(BaseService):
    """Transfer-out request operations."""

    def list(
        self,
        body: dict | None = None,
        *,
        keys: list[str] | None = None,
        headers: dict | None = None,
    ):
        """List outgoing transfer requests.

        :param body: Optional query filters.
        :param keys: Additional data keys to return.
        :param headers: Optional extra HTTP headers.
        :returns: Response with list of :class:`~domainrobot.models.resources.TransferOut`.
        """
        return self._request(
            "POST",
            "/transferout/_search",
            json=body or {},
            params=self._keys_params(keys),
            headers=headers,
            model=TransferOut,
        )

    def answer(
        self,
        domain: str,
        answer_type: Literal["ACK", "NACK"],
        body: dict | None = None,
        *,
        headers: dict | None = None,
    ):
        """Accept (ACK) or reject (NACK) a transfer request.

        :param domain: Domain name.
        :param answer_type: ``"ACK"`` or ``"NACK"``.
        :param body: Optional transfer-out data (e.g. nackReason).
        :param headers: Optional extra HTTP headers.
        :returns: Response with :class:`~domainrobot.models.resources.TransferOut` data.
        """
        return self._request(
            "PUT",
            f"/transferout/{domain}/{answer_type}",
            json=body,
            headers=headers,
            model=TransferOut,
        )
