"""A small Python module with one function and one class, including a specific token in a docstring. | token=f5b0697b"""

def greet(name):
    """Return a simple greeting message including the token f5b0697b."""
    return f"Hello, {name}! Token: f5b0697b"

class Counter:
    """A simple counter class that includes token f5b0697b in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
