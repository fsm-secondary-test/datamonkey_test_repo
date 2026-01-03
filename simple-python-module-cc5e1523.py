"""A small Python module with one simple function and one simple class, including a specific token in a docstring. | token=cc5e1523"""

def greet(name):
    """Return a greeting message including the provided name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token cc5e1523."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
