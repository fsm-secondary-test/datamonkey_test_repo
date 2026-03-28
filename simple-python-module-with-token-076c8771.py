"""This module contains a simple function and a simple class. The token '076c8771' is included in a docstring. | token=076c8771"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class SimpleCounter:
    """A simple counter class with a token '076c8771' in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
