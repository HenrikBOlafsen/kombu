"""Private helper module for static analysis hacks.

This module contains imports that are only used for static analysis
purposes to avoid dependency cycles in the main module structure.
"""

# Re-export BrokerConnection and Connection to maintain backward compatibility
# for static analysis tools
from .connection import BrokerConnection, Connection