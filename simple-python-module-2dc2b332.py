"""A small Python module with one simple function and one simple class, including a literal token in a docstring. | token=2dc2b332"""

def greet(name):
    """Return a greeting message including the token 2dc2b332."""
    return f"Hello, {name}! Your token is 2dc2b332."

class Counter:
    """A simple counter class with token 2dc2b332 in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
