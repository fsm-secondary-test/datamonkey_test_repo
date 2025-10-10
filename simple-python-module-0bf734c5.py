"""A small Python module containing one function and one class, including a specific token in the docstring. | token=0bf734c5"""

def greet(name):
    """Return a greeting message including the token 0bf734c5."""
    return f"Hello, {name}! Token: 0bf734c5"

class Counter:
    """A simple counter class with token 0bf734c5 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
