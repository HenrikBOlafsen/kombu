
"""Private helpers for channel/connection operations."""
from __future__ import annotations

from typing import Any, Protocol

class HasDefaultChannel(Protocol):
    """Protocol for objects that have a default_channel attribute."""
    default_channel: Any

def maybe_channel(channel: Any) -> Any:
    """Get channel from object.

    Return the default channel if argument is a connection instance,
    otherwise just return the channel given.
    """
    if is_connection(channel):
        return channel.default_channel
    return channel

def is_connection(obj: Any) -> bool:
    """Check if object is a connection by duck typing."""
    return hasattr(obj, 'default_channel') and hasattr(obj, 'connected')

def is_pooled_connection(obj: Any) -> bool:
    """Check if object is a pooled connection by duck typing."""
    return hasattr(obj, '_pool') and hasattr(obj, 'replace')