"""A small Python module with one function and one class, including a literal token in a docstring. | token=987e93ec"""

def greet(name):
    """Return a greeting message including a secret token 987e93ec."""
    return f"Hello, {name}! Your token is 987e93ec."

class Counter:
    """A simple counter class with token 987e93ec in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
