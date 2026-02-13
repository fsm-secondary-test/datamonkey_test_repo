"""This module contains one simple function and one simple class, including the token 'faf3e500' in a docstring. | token=faf3e500"""

def greet(name):
    """Return a greeting message including the token faf3e500."""
    return f"Hello, {name}! Token: faf3e500"

class Counter:
    """A simple counter class that includes the token faf3e500."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increase the count by one."""
        self.count += 1

    def reset(self):
        """Reset the count to zero."""
        self.count = 0

    def __str__(self):
        return f"Counter value: {self.count} (Token: faf3e500)"
