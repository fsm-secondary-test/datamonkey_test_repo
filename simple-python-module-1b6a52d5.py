"""A small Python module with one simple function and one simple class, including a token in the docstring. | token=1b6a52d5"""

def greet(name):
    """Return a greeting message including the token 1b6a52d5."""
    return f"Hello, {name}! Token: 1b6a52d5"

class Counter:
    """Simple counter class with token 1b6a52d5 in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
