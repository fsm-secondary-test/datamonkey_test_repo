"""A small Python module containing one function and one class, including the token '9cd3ccc7' in a docstring. | token=9cd3ccc7"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token 9cd3ccc7 in the docstring."""

    def __init__(self, start=0):
        self.count = start

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
