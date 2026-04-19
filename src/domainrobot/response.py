from __future__ import annotations

from typing import Any, Generic, TypeVar

from .models._base import Model

T = TypeVar("T", bound=Model)


class DomainrobotResponse(Generic[T]):
    """Wrapper around a successful API response.

    When a ``model`` class is provided the items in :attr:`data`
    are instances of that model, giving IDE autocompletion and
    type safety.  Otherwise they remain plain dicts.
    """

    __slots__ = ("status_code", "stid", "ctid", "status", "data", "messages", "headers")

    def __init__(
        self,
        status_code: int,
        body: dict[str, Any],
        headers: dict[str, str],
        model: type[T] | None = None,
    ):
        #: HTTP status code.
        self.status_code = status_code
        #: Server transaction ID.
        self.stid: str | None = body.get("stid")
        #: Client transaction ID.
        self.ctid: str | None = body.get("ctid")
        #: Response status object.
        self.status: dict | None = body.get("status")
        #: Response messages.
        self.messages: list[dict] | None = body.get("messages")
        #: HTTP response headers.
        self.headers = headers

        raw_data: list[dict] | None = body.get("data")
        if raw_data is not None and model is not None:
            #: Response data — typed model instances when a model is set,
            #: otherwise plain dicts.
            self.data: list[T] | None = [model.from_dict(item) for item in raw_data]
        else:
            self.data = raw_data  # type: ignore[assignment]

    def __repr__(self) -> str:
        return (
            f"DomainrobotResponse(status_code={self.status_code}, stid={self.stid!r})"
        )
