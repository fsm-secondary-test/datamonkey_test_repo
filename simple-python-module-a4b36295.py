"""A small Python module with one function and one class, including a specific token in a docstring. | token=a4b36295"""

def greet(name):
    """Return a greeting message including the token a4b36295."""
    return f"Hello, {name}! Token: a4b36295"

class Counter:
    """Simple counter class with token a4b36295 in docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
