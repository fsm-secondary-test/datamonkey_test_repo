"""A small Python module with one simple function and one simple class, including the token 'ebf23fba' in a docstring. | token=ebf23fba"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token ebf23fba in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def value(self):
        return self.count
