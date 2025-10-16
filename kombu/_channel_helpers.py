"""Helper functions for channel/connection operations."""

from typing import Any

__all__ = ('is_connection', 'maybe_channel')


def maybe_channel(channel: Any) -> Any:
    """Get channel from object.

    Return the default channel if argument is a connection instance,
    otherwise just return the channel given.
    """
    if is_connection(channel):
        return channel.default_channel
    return channel


def is_connection(obj: Any) -> bool:
    """Check if object is a connection instance."""
    # Use duck typing instead of isinstance to avoid circular imports
    return hasattr(obj, 'default_channel') and hasattr(obj, 'channel')