from __future__ import annotations

import dataclasses
from typing import Any, TypeVar

T = TypeVar("T", bound="Model")


@dataclasses.dataclass
class Model:
    """Base for all API resource models.

    Unknown API fields are captured in :attr:`extra` so the client
    stays forward-compatible when the API adds new fields.
    """

    extra: dict[str, Any] = dataclasses.field(default_factory=dict, repr=False)

    @classmethod
    def from_dict(cls: type[T], data: dict[str, Any]) -> T:
        """Create a model instance from an API response dict.

        Known fields are set as attributes; everything else goes
        into :attr:`extra`.
        """
        try:
            known = cls.__known_fields__
        except AttributeError:
            known = frozenset(f.name for f in dataclasses.fields(cls))
            cls.__known_fields__ = known  # type: ignore[attr-defined]
        kwargs: dict[str, Any] = {}
        extra: dict[str, Any] = {}
        for key, value in data.items():
            if key in known:
                kwargs[key] = value
            else:
                extra[key] = value
        kwargs["extra"] = extra
        return cls(**kwargs)
