"""A small Python module with one simple function and one simple class, including the token '61b1a8fe' in a docstring. | token=61b1a8fe"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token 61b1a8fe in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
