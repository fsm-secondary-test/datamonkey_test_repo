"""A small Python module with one function and one class, including the token '6528d5b1' in a docstring. | token=6528d5b1"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class storing count and token '6528d5b1'."""
    def __init__(self):
        self.count = 0
        self.token = '6528d5b1'

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
