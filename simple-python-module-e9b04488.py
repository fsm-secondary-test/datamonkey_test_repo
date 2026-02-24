"""A Python module with one simple function and one simple class, including a literal token in the docstring. | token=e9b04488"""

def greet(name):
    """Return a greeting message including the token e9b04488."""
    return f"Hello, {name}! Token: e9b04488"

class Counter:
    """A simple counter class with token e9b04488 in the docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
