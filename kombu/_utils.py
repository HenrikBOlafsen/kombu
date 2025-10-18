"""Internal utility functions shared between modules."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from kombu.connection import Connection
    from kombu.transport.virtual import Channel

from .utils.functional import maybe_list


def maybe_channel(channel: 'Channel | Connection') -> 'Channel':
    """Get channel from object.

    Return the default channel if argument is a connection instance,
    otherwise just return the channel given.
    """
    from .connection import Connection
    if isinstance(channel, Connection):
        return channel.default_channel
    return channel


def is_connection(obj: Any) -> bool:
    """Check if object is a Connection instance."""
    from .connection import Connection
    return isinstance(obj, Connection)