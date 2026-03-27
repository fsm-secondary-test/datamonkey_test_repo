"""A small Python module with one function and one class, including a specific token in a docstring. | token=4bc1235e"""

def greet(name):
    """Return a greeting message including the token 4bc1235e."""
    return f"Hello, {name}! Token 4bc1235e."

class Counter:
    """A simple counter class with token 4bc1235e in docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increase the counter by one."""
        self.count += 1

    def value(self):
        """Return the current count value."""
        return self.count
