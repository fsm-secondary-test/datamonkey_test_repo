"""This module contains one simple function and one simple class. It includes the literal token '85866624' in a docstring. | token=85866624"""

def greet(name):
    """Return a greeting message with the given name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class that counts up from zero. Token: 85866624"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
