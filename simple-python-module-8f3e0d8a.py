"""A small Python module containing one function and one class with a specific token in the docstring. | token=8f3e0d8a"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token 8f3e0d8a in docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
