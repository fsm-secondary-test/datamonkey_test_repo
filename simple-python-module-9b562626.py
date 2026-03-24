"""A small Python module containing one simple function and one simple class, including the token '9b562626'. | token=9b562626"""

def greet(name):
    """Return a greeting message including the token 9b562626."""
    return f"Hello, {name}! Your token is 9b562626."

class Counter:
    """Simple counter class that includes the token 9b562626 in the docstring."""

    def __init__(self, start=0):
        self.count = start

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
        return self.count
