"""A small Python module containing one function and one class, including a specific token in a docstring. | token=4d971003"""

def greet(name):
    """Return a greeting message including the token 4d971003."""
    return f"Hello, {name}! Token: 4d971003"

class Counter:
    """A simple counter class with token 4d971003 in the docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by 1."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
