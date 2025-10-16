"""A module with one function and one class, including a specific token in a docstring. | token=27fc7e9d"""

def greet(name):
    """Return a greeting message including the token 27fc7e9d."""
    return f"Hello, {name}! Token: 27fc7e9d"

class Counter:
    """A simple counter class that tracks counts with token 27fc7e9d."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count
