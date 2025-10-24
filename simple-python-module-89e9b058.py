"""A small Python module with one function and one class, including a specific token in the docstring. | token=89e9b058"""

def greet(name):
    """Return a greeting message including the token 89e9b058."""
    return f"Hello, {name}! Your token is 89e9b058."

class Counter:
    """A simple counter class that increments and resets."""

    def __init__(self):
        self.count = 0
        self.token = '89e9b058'

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def __str__(self):
        return f"Counter value: {self.count} (token: {self.token})"
