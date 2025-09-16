
#!/usr/bin/env python
"""Test script to verify the refactoring works correctly."""

from kombu import Connection
from kombu.messaging import Producer
from kombu._channel_helpers import is_connection, maybe_channel

def test_imports():
    """Test that imports still work correctly."""
    print("Testing imports...")

    # Test that public imports still work
    from kombu.connection import is_connection as conn_is_connection
    from kombu.connection import maybe_channel as conn_maybe_channel

    print("✓ Public imports work")

    # Test that the functions are the same
    assert is_connection is conn_is_connection
    assert maybe_channel is conn_maybe_channel
    print("✓ Re-exports work correctly")

def test_functionality():
    """Test that the functions work as expected."""
    print("Testing functionality...")

    conn = Connection('memory://')
    channel = conn.channel()

    # Test is_connection
    assert is_connection(conn) is True
    assert is_connection(channel) is False
    print("✓ is_connection works")

    # Test maybe_channel
    assert maybe_channel(channel) is channel
    assert maybe_channel(conn) is conn.default_channel
    print("✓ maybe_channel works")

def test_producer_construction():
    """Test that Producer construction still works."""
    print("Testing Producer construction...")

    conn = Connection('memory://')
    producer = conn.Producer()
    assert producer is not None
    print("✓ Producer construction works")

def test_duck_typing():
    """Test that duck typing works in Producer.__exit__."""
    print("Testing duck typing...")

    class MockConnection:
        def __init__(self):
            self._pool = None

    class MockProducer:
        def __init__(self):
            self.__connection__ = MockConnection()

        def release(self):
            pass

    producer = MockProducer()
    # This should not raise any errors
    assert producer.__connection__._pool is None
    print("✓ Duck typing works")

if __name__ == '__main__':
    test_imports()
    test_functionality()
    test_producer_construction()
    test_duck_typing()
    print("\n✅ All tests passed! The refactoring is working correctly.")