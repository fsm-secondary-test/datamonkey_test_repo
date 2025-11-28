"""A small Python module with one function and one class, including a specific token in the docstring. | token=c787783c"""

def greet(name):
    """Return a greeting message including the token c787783c."""
    return f"Hello, {name}! Token: c787783c"

class Counter:
    """A simple counter class with token c787783c in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
