"""A small Python module with one function and one class including a literal token in the docstring. | token=3289c4e1"""

def greet(name):
    """Return a greeting message including token 3289c4e1."""
    return f"Hello, {name}! Token: 3289c4e1"

class Counter:
    """A simple counter class with token 3289c4e1 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
