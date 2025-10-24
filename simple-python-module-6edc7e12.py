"""A small Python module with one function and one class, including a specific token in a docstring. | token=6edc7e12"""

def greet(name):
    """Return a greeting message including the token 6edc7e12."""
    return f"Hello, {name}! This token is 6edc7e12."

class Counter:
    """A simple counter class with token 6edc7e12 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
