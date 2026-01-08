"""A small Python module with one simple function and one simple class including a specific token in the docstring. | token=b548dbb3"""

def greet(name):
    """Return a greeting message with the provided name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token b548dbb3."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count
