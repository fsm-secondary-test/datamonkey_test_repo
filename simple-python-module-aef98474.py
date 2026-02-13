"""A module containing one simple function and one simple class, including the token 'aef98474' in a docstring. | token=aef98474"""

def greet(name):
    """Return a greeting message including the given name and the token 'aef98474'."""
    return f"Hello, {name}! Token: aef98474"

class Counter:
    """A simple counter class with token 'aef98474' in the docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the count by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
