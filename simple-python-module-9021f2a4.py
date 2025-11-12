"""A small Python module with one function and one class, including a specific token in docstrings. | token=9021f2a4"""

def greet(name):
    """Return a greeting message including the token 9021f2a4."""
    return f"Hello, {name}! Token: 9021f2a4"

class Counter:
    """A simple counter class with token 9021f2a4 in its docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by 1."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
