"""A small Python module with one function and one class, including a specific token in a docstring. | token=0f5782a3"""

def greet(name):
    """Return a greeting message including the token 0f5782a3."""
    return f"Hello, {name}! This is token 0f5782a3."

class Counter:
    """A simple counter class with token 0f5782a3 in its docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def __str__(self):
        return f"Counter value: {self.count}"
