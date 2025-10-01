
"""Channel and connection helper functions."""
from __future__ import annotations

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from types import TracebackType
    from typing import TypeGuard

def maybe_channel(channel: Any) -> Any:
    """Get channel from object.

    Return the default channel if argument is a connection instance,
    otherwise just return the channel given.
    """
    if is_connection(channel):
        return channel.default_channel
    return channel

def is_connection(obj: Any) -> bool:
    """Check if object is a connection.

    Uses duck typing to check for connection-like attributes
    without creating a circular import.
    """
    return hasattr(obj, 'default_channel') and hasattr(obj, 'connected')

def is_pooled_connection(obj: Any) -> bool:
    """Check if object is a pooled connection.

    Uses duck typing to check for pooled connection attributes
    without creating a circular import.
    """
    return hasattr(obj, '_pool') and hasattr(obj, 'replace')
