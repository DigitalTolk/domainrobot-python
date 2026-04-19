from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .._http import HttpClient
    from ..models._base import Model
    from ..response import DomainrobotResponse


class BaseService:
    """Shared functionality for all service classes."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def _request(
        self,
        method: str,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        model: type[Model] | None = None,
    ) -> DomainrobotResponse:
        return self._http.request(
            method, path, json=json, params=params, headers=headers, model=model
        )

    @staticmethod
    def _keys_params(
        keys: list[str] | None,
        extra: dict[str, Any] | None = None,
    ) -> dict[str, Any] | None:
        params: dict[str, Any] = {}
        if keys:
            params["keys[]"] = keys
        if extra:
            params.update(extra)
        return params or None
