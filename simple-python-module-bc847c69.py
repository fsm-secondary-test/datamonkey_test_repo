"""A small Python module with one function and one class, including a specific token in the docstring. | token=bc847c69"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token bc847c69."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
