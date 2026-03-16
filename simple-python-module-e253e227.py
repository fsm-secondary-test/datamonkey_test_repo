"""A small Python module containing one function and one class, including a specific token in a docstring. | token=e253e227"""

def greet(name):
    """Return a greeting message including the token e253e227."""
    return f"Hello, {name}! Token: e253e227"

class Counter:
    """A simple counter class that includes the token e253e227 in its docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count
