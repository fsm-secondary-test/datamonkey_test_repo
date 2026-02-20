"""A Python module containing one simple function and one simple class, including the token '7dcdefac' in a docstring. | token=7dcdefac"""

def greet(name):
    """Return a greeting message including the token '7dcdefac'."""
    return f"Hello, {name}! Token: 7dcdefac"

class Counter:
    """A simple counter class that keeps track of counts. Token: 7dcdefac"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
