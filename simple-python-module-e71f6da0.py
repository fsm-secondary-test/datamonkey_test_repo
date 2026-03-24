"""A Python module with one function and one class including a specific token in a docstring. | token=e71f6da0"""

def greet(name):
    """Return a greeting message including the given name and token e71f6da0."""
    return f"Hello, {name}! This is token e71f6da0."

class Counter:
    """A simple counter class that uses token e71f6da0 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0

