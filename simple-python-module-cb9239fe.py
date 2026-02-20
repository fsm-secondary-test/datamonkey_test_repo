"""A small Python module with a simple function and class, including a literal token in a docstring. | token=cb9239fe"""

def greet(name):
    """Return a greeting message including the token cb9239fe."""
    return f"Hello, {name}! Token: cb9239fe"

class Counter:
    """A simple counter class that includes the token cb9239fe in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
