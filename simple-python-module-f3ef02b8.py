"""A small Python module containing one function and one class. Includes a token in the docstring. | token=f3ef02b8"""

def greet(name):
    """Return a greeting message for the given name. Token: f3ef02b8"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class containing token f3ef02b8."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
