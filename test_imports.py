#!/usr/bin/env python3

print("Testing imports...")
try:
    import kombu
    print("Successfully imported kombu")
    
    # Try to import connection
    from kombu import connection
    print("Successfully imported kombu.connection")
    
    # Try to import exceptions
    from kombu import exceptions
    print("Successfully imported kombu.exceptions")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()