"""A Python module containing a simple function and a simple class with a unique token in a docstring. | token=7bb94f97"""

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token 7bb94f97 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
