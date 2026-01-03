"""A small Python module containing one simple function and one simple class, including a literal token in a docstring. | token=06351a36"""

def greet(name):
    """Return a greeting message including the token 06351a36."""
    return f"Hello, {name}! Token: 06351a36"

class Counter:
    """A simple counter class with token 06351a36 in its docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def value(self):
        return self.count

