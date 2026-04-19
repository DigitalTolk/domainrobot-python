from __future__ import annotations

import dataclasses
import datetime
import types
from typing import Any, TypeVar, Union, get_type_hints

T = TypeVar("T", bound="Model")

_ISO_FORMATS = [
    "%Y-%m-%dT%H:%M:%S.%f%z",
    "%Y-%m-%dT%H:%M:%S%z",
    "%Y-%m-%dT%H:%M:%S.%f",
    "%Y-%m-%dT%H:%M:%S",
]


def _parse_datetime(value: Any) -> datetime.datetime | None:
    """Try to parse a datetime string from the API."""
    if value is None or isinstance(value, datetime.datetime):
        return value
    if not isinstance(value, str):
        return value  # type: ignore[return-value]
    for fmt in _ISO_FORMATS:
        try:
            return datetime.datetime.strptime(value, fmt)
        except ValueError:
            continue
    return value  # type: ignore[return-value]


@dataclasses.dataclass
class Model:
    """Base for all API resource models.

    Unknown API fields are captured in :attr:`extra` so the client
    stays forward-compatible when the API adds new fields.

    Fields typed as :class:`~datetime.datetime` are automatically
    parsed from ISO-8601 strings returned by the API.
    """

    extra: dict[str, Any] = dataclasses.field(default_factory=dict, repr=False)

    @classmethod
    def from_dict(cls: type[T], data: dict[str, Any]) -> T:
        """Create a model instance from an API response dict.

        Known fields are set as attributes; everything else goes
        into :attr:`extra`.  Datetime strings are auto-parsed.
        """
        try:
            known = cls.__known_fields__
            dt_fields = cls.__datetime_fields__
        except AttributeError:
            known = frozenset(f.name for f in dataclasses.fields(cls))
            cls.__known_fields__ = known  # type: ignore[attr-defined]
            hints = get_type_hints(cls)
            dt_fields = frozenset(
                name for name, hint in hints.items()
                if _is_datetime_hint(hint)
            )
            cls.__datetime_fields__ = dt_fields  # type: ignore[attr-defined]

        kwargs: dict[str, Any] = {}
        extra: dict[str, Any] = {}
        for key, value in data.items():
            if key in known:
                if key in dt_fields and isinstance(value, str):
                    kwargs[key] = _parse_datetime(value)
                else:
                    kwargs[key] = value
            else:
                extra[key] = value
        kwargs["extra"] = extra
        return cls(**kwargs)


def _is_datetime_hint(hint: Any) -> bool:
    """Check if a type hint is or contains datetime.datetime."""
    if hint is datetime.datetime:
        return True
    origin = getattr(hint, "__origin__", None)
    args = getattr(hint, "__args__", ())
    # Union[datetime, None] or datetime | None
    if origin is Union or isinstance(hint, types.UnionType):
        return any(a is datetime.datetime for a in args)
    return False
