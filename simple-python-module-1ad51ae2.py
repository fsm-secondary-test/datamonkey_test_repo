"""A small Python module with one function and one class, including a token in a docstring. | token=1ad51ae2"""

def greet(name):
    """Return a greeting message including the token 1ad51ae2."""
    return f"Hello, {name}! Token: 1ad51ae2"

class Counter:
    """A simple counter class with token 1ad51ae2 in the docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
