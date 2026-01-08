"""A small Python module with a simple function and a simple class, including a specific token in a docstring. | token=5a85c3dc"""

def greet(name):
    """Return a greeting message including the token 5a85c3dc."""
    return f"Hello, {name}! Token: 5a85c3dc"

class Counter:
    """A simple counter class that tracks counts and includes token 5a85c3dc."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
