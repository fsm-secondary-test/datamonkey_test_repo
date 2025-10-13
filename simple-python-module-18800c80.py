"""A small Python module with one function and one class, including a specific token in a docstring. | token=18800c80"""

def greet(name):
    """Return a greeting message including the token 18800c80."""
    return f"Hello, {name}! Token: 18800c80"

class Counter:
    """A simple counter class with token 18800c80 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
