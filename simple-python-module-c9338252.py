"""A small Python module with one function and one class, including a specific token in the docstring. | token=c9338252"""

def greet(name):
    """Return a greeting message including the token c9338252."""
    return f"Hello, {name}! This is token c9338252."

class Counter:
    """A simple counter class that uses token c9338252 in its docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
