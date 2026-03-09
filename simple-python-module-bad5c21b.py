"""A small Python module containing one function and one class, including a specific token in a docstring. | token=bad5c21b"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token bad5c21b in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
