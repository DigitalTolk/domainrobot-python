from __future__ import annotations

from ._base import BaseService


class PollService(BaseService):
    def info(self, *, headers: dict | None = None):
        return self._request("GET", "/poll", headers=headers)

    def confirm(self, poll_id: int, *, headers: dict | None = None):
        return self._request("PUT", f"/poll/{poll_id}", headers=headers)
