"""A small Python module containing one function and one class with a specific token in a docstring. | token=6eacbcc1"""

def greet(name):
    """Return a greeting message for the given name. Token: 6eacbcc1"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 6eacbcc1"""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the count by 1."""
        self.count += 1

    def reset(self):
        """Reset the count to zero."""
        self.count = 0
