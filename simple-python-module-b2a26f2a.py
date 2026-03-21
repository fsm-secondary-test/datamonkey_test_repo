"""A module with one function and one class, including the token 'b2a26f2a' in a docstring. | token=b2a26f2a"""

def greet(name):
    """Return a greeting message including the token b2a26f2a."""
    return f"Hello, {name}! Token: b2a26f2a"

class Counter:
    """A simple counter class that tracks counts. Token: b2a26f2a"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
