"""A small Python module with one function and one class, including a specific token in a docstring. | token=3be4e128"""

def greet(name):
    """Return a greeting message including the token 3be4e128."""
    return f"Hello, {name}! Token: 3be4e128"

class Counter:
    """A simple counter class with token 3be4e128 in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
