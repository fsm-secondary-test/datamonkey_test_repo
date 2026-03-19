"""A Python module with one function and one class, including a specific token in the docstring. | token=bd254fbb"""

def greet(name):
    """Return a greeting message including the token bd254fbb."""
    return f"Hello, {name}! Token: bd254fbb"

class Counter:
    """A simple counter class with token bd254fbb in the docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
