"""A small Python module containing one function and one class with a specific token in the docstring. | token=f0bed3aa"""

def greet(name):
    """Return a greeting message including the token f0bed3aa."""
    return f"Hello, {name}! Token: f0bed3aa"

class Counter:
    """A simple counter class with token f0bed3aa in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
