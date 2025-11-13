"""A small Python module with one simple function and one simple class, including a specific token in a docstring. | token=2ea2c41b"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class SimpleCounter:
    """A simple counter class with token 2ea2c41b in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
