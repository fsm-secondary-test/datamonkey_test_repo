"""A small Python module with one function and one class, including a specific token in the docstring. | token=9021f2a4"""

def greet(name):
    """Return a greeting message including a special token: 9021f2a4."""
    return f"Hello, {name}! Your token is 9021f2a4."

class Counter:
    """Simple counter class with token 9021f2a4 in docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
