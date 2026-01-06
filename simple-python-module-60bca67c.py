"""A small Python module containing one function and one class with the token '60bca67c' included in a docstring. | token=60bca67c"""

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token 60bca67c in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
