# kombu/utils/channel_api.py
from __future__ import annotations

from typing import Any
try:
    from typing import Protocol, TypeGuard  # py3.10+
except ImportError:  # pragma: no cover
    from typing_extensions import Protocol, TypeGuard


class SupportsDefaultChannel(Protocol):
    @property
    def default_channel(self) -> Any: ...


def is_connection(obj: Any) -> TypeGuard[SupportsDefaultChannel]:
    # structural check; no import from kombu.connection
    return hasattr(obj, "default_channel")


def maybe_channel(channel: Any) -> Any:
    dc = getattr(channel, "default_channel", None)
    return dc if dc is not None else channel
