"""A small Python module with one function and one class, including a token in a docstring. | token=819cb834"""

def greet(name):
    """Return a greeting message including the token 819cb834."""
    return f"Hello, {name}! Token: 819cb834"

class Counter:
    """A simple counter class with token 819cb834 in the docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count
