"""A small Python module with one function and one class, including a specific token in a docstring. | token=5a83b5dd"""

def greet(name):
    """Return a greeting message including the token 5a83b5dd."""
    return f"Hello, {name}! Token: 5a83b5dd"

class Counter:
    """A simple counter class with token 5a83b5dd in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
