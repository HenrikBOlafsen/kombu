"""Helper functions and classes for connection-related utilities."""

from typing import TYPE_CHECKING, Any

from .connection import Connection
from .transport.virtual import Channel

if TYPE_CHECKING:
    from .connection import Connection
    from .transport.virtual import Channel


def maybe_channel(channel: 'Channel | Connection') -> 'Channel':
    """Get channel from object.

    Return the default channel if argument is a connection instance,
    otherwise just return the channel given.
    """
    if isinstance(channel, Connection):
        return channel.default_channel
    return channel


def is_connection(obj: Any) -> bool:
    """Check if object is a Connection instance."""
    return isinstance(obj, Connection)


class PooledConnection(Connection):
    """Wraps :class:`kombu.Connection`.

    This wrapper modifies :meth:`kombu.Connection.__exit__` to close the connection
    in case any exception occurred while the context was active.
    """

    def __init__(self, pool, **kwargs):
        self._pool = pool
        super().__init__(**kwargs)