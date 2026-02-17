"""A small Python module with one function and one class, including a specific token in the docstring. | token=6febdcab"""

def greet(name):
    """Return a greeting message including the token 6febdcab."""
    return f"Hello, {name}! Token: 6febdcab"

class Counter:
    """A simple counter class with token 6febdcab in docstring."""

    def __init__(self, start=0):
        self.count = start

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count
