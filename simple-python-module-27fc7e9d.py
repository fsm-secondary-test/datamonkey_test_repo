"""A small Python module containing one function and one class with a special token in the docstring. | token=27fc7e9d"""

def greet(name):
    """Return a greeting message including the special token 27fc7e9d."""
    return f"Hello, {name}! Your token is 27fc7e9d."

class Counter:
    """A simple counter class with token 27fc7e9d."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
