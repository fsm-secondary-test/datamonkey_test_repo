"""A small Python module with one function and one class, including a specific token in the docstring. | token=a51aad96"""

def greet(name):
    """Return a greeting message including the token a51aad96."""
    return f"Hello, {name}! Your token is a51aad96."

class Counter:
    """A simple counter class that uses the token a51aad96 internally."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
