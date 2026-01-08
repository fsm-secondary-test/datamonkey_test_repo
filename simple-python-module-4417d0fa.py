"""A small Python module containing one function and one class, with a specific token in the docstring. | token=4417d0fa"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token 4417d0fa."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
