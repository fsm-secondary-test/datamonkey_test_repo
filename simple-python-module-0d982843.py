"""A small Python module with one function and one class, containing a specific token in a docstring. | token=0d982843"""

def greet(name):
    """Return a greeting message including the token '0d982843'."""
    return f"Hello, {name}! Your token is 0d982843."

class Counter:
    """A simple counter class with token 0d982843 in the docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
