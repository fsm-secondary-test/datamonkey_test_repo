"""A small Python module containing one simple function and one simple class with a specific token in a docstring. | token=0bcb9882"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token 0bcb9882 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count
