"""A small Python module containing one function and one class, including a literal token in a docstring. | token=7cfac9a2"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 7cfac9a2"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
