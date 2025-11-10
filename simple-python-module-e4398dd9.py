"""A small Python module containing one function and one class, including a token in a docstring. | token=e4398dd9"""

def greet(name):
    """Return a greeting message including the token e4398dd9."""
    return f"Hello, {name}! Token: e4398dd9"

class Counter:
    """Simple counter class with token e4398dd9 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
