"""A small Python module with one function and one class, including a specific token in the docstring. | token=35def055"""

def greet(name):
    """Return a greeting message including the token 35def055."""
    return f"Hello, {name}! Token: 35def055"

class Counter:
    """Simple counter class with token 35def055 in the docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
