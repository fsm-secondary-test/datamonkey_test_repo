"""A small Python module containing one simple function and one simple class, including a specific token in a docstring. | token=8f17ddb3"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token 8f17ddb3."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by 1."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
