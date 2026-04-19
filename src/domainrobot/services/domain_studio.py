from __future__ import annotations

from ._base import BaseService


class DomainStudioService(BaseService):
    def search(self, body: dict, *, headers: dict | None = None):
        return self._request("POST", "/domainstudio", json=body, headers=headers)
