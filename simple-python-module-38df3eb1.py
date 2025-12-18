"""A small Python module with one simple function and one simple class, including a token in a docstring. | token=38df3eb1"""

def greet(name):
    """Return a greeting message with a token: 38df3eb1"""
    return f"Hello, {name}! Welcome to the 38df3eb1 module."

class Counter:
    """Simple counter class with token 38df3eb1 in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
