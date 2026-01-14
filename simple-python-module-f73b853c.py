"""A Python module with one simple function and one simple class, including a specific token in a docstring. | token=f73b853c"""

def greet(name):
    """Return a greeting message including the token f73b853c."""
    return f"Hello, {name}! Token: f73b853c"

class Counter:
    """A simple counter class with token f73b853c in the docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the count by one."""
        self.count += 1

    def reset(self):
        """Reset the count to zero."""
        self.count = 0

    def get_count(self):
        """Return the current count."""
        return self.count
