"""A Python module with one simple function and one simple class, including a specific token in a docstring. | token=197e74f7"""

def greet(name):
    """Return a greeting message including the token '197e74f7'."""
    return f"Hello, {name}! Token: 197e74f7"

class Counter:
    """Simple counter class with token '197e74f7' in the docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
