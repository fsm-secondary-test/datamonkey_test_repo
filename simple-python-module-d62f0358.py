"""A small Python module with one function and one class, including a specific token in a docstring. | token=d62f0358"""

def greet(name):
    """Return a greeting message including the token d62f0358."""
    return f"Hello, {name}! Welcome to the d62f0358 module."

class Counter:
    """A simple counter class with token d62f0358 in its docstring."""

    def __init__(self, start=0):
        self.count = start

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
