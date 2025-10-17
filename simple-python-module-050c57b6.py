"""A small Python module with one function and one class, including a token in a docstring. | token=050c57b6"""

def greet(name):
    """Return a greeting message including the token 050c57b6."""
    return f"Hello, {name}! Your token is 050c57b6."

class Counter:
    """A simple counter class with token 050c57b6 in the docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the count by 1."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
