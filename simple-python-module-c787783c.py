"""A small Python module with one function and one class, including a specific token in a docstring. | token=c787783c"""

def greet(name):
    """Return a greeting message including the token c787783c."""
    return f"Hello, {name}! Token: c787783c"

class Counter:
    """A simple counter class that includes the token c787783c in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def value(self):
        return self.count
