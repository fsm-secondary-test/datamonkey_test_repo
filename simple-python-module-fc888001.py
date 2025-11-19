"""A small Python module containing one function and one class, including the token 'fc888001' in a docstring. | token=fc888001"""

def greet(name):
    """Return a greeting message including the provided name."""
    return f"Hello, {name}!"

class SimpleCounter:
    """A simple counter class with token fc888001."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
