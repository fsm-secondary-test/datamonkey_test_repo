"""A small Python module with one function and one class, including a specific token in a docstring. | token=4cf3a5a6"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token 4cf3a5a6 in this docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
