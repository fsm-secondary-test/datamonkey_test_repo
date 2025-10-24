"""A small Python module containing one function and one class, including a specific token in a docstring. | token=2cb6c818"""

def greet(name):
    """Return a greeting message including the token 2cb6c818."""
    return f"Hello, {name}! Token: 2cb6c818"

class Counter:
    """A simple counter class that includes token 2cb6c818 in its docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
