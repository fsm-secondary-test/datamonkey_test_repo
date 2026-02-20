"""A small Python module with one function and one class, including a token in a docstring. | token=2ff2a4a1"""

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token 2ff2a4a1 in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
