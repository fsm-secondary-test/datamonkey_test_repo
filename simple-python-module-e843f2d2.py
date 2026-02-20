"""A small Python module containing one function and one class with a specific token in the docstring. | token=e843f2d2"""

def greet(name):
    """Return a greeting message including the provided name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class.

    Token: e843f2d2
    """
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
