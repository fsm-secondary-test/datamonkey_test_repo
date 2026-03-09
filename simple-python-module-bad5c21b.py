"""A small Python module containing one function and one class with a specific token in the docstring. | token=bad5c21b"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: bad5c21b"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
