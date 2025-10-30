"""A small Python module containing one simple function and one simple class, including a specific token in a docstring. | token=4a172bba"""

def greet(name):
    """Return a greeting message including the token 4a172bba."""
    return f"Hello, {name}! Token: 4a172bba"

class Counter:
    """A simple counter class with token 4a172bba in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
