"""A module containing one simple function and one simple class with a specific token in docstring. | token=e341218d"""

def greet(name):
    """Return a greeting message including the name. Token: e341218d"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token e341218d."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
