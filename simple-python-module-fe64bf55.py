"""This module contains one simple function and one simple class. The token 'fe64bf55' is included in the module docstring. | token=fe64bf55"""

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class that increments a count."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increase the count by one."""
        self.count += 1

    def reset(self):
        """Reset the count to zero."""
        self.count = 0

    def get_count(self):
        """Return the current count."""
        return self.count
