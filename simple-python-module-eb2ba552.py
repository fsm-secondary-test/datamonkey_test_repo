"""A small Python module with one function and one class including a specific token in a docstring. | token=eb2ba552"""

def greet(name):
    """Return a greeting message including the token eb2ba552."""
    return f"Hello, {name}! Token: eb2ba552"

class Counter:
    """A simple counter class that includes token eb2ba552 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
