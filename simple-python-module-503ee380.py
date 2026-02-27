"""A Python module containing one function and one class, including a specific token in a docstring. | token=503ee380"""

def greet(name):
    """Return a greeting message including the token 503ee380."""
    return f"Hello, {name}! This is token 503ee380."

class Counter:
    """A simple counter class with token 503ee380 in the docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count
