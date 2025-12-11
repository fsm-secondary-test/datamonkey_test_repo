"""A small Python module with one function and one class, including a specific token in a docstring. | token=9b39b9c9"""

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token 9b39b9c9 in docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def value(self):
        return self.count
