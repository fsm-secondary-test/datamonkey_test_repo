"""A small Python module with one function and one class including a special token in the docstring. | token=6e72e0ff"""

def greet(name):
    """Return a greeting message including the token 6e72e0ff."""
    return f"Hello, {name}! Your token is 6e72e0ff."

class Counter:
    """A simple counter class that includes the token 6e72e0ff in its docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
