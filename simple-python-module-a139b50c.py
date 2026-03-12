"""A small Python module with one function and one class, including a specific token in the docstring. | token=a139b50c"""

def greet(name):
    """Return a greeting message including the token a139b50c."""
    return f"Hello, {name}! This is token a139b50c."

class Counter:
    """A simple counter class that includes the token a139b50c."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
