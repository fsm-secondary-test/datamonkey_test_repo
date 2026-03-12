"""A small Python module containing one function and one class, including a specific token in a docstring. | token=ec190b03"""

def greet(name):
    """Return a greeting message including the provided name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token ec190b03 included."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
