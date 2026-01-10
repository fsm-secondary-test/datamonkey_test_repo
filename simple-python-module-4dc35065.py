"""A small Python module with one function and one class, including a specific token in a docstring. | token=4dc35065"""

def greet(name):
    """Return a greeting message including the provided name and a token 4dc35065."""
    return f"Hello, {name}! Token: 4dc35065"

class Counter:
    """A simple counter class with token 4dc35065."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count
