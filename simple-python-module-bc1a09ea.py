"""A small Python module with one function and one class including a specific token in a docstring. | token=bc1a09ea"""

def greet(name):
    """Return a greeting message including the token bc1a09ea."""
    return f"Hello, {name}! Token: bc1a09ea"

class Counter:
    """A simple counter class with token bc1a09ea in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
