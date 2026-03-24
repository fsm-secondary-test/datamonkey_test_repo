"""A small Python module with one simple function and one simple class. Includes the token '022e14dc' in a docstring. | token=022e14dc"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 022e14dc"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
