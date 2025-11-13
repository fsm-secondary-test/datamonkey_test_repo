"""A small Python module with one simple function and one simple class including a specific token in the docstring. | token=2ea2c41b"""

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token 2ea2c41b."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
