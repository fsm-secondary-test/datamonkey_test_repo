"""A small Python module with one function and one class, including a literal token in a docstring. | token=6fe1e233"""

def greet(name):
    """Return a greeting message including the token 6fe1e233."""
    return f"Hello, {name}! Your token is 6fe1e233."

class Counter:
    """A simple counter class with token 6fe1e233 in the docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by 1."""
        self.count += 1

    def value(self):
        """Return the current count value."""
        return self.count
