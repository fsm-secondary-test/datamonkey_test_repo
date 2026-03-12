"""A small Python module containing one function and one class, including a specific token in a docstring. | token=6d907e28"""

def greet(name):
    """Return a greeting message including the token 6d907e28."""
    return f"Hello, {name}! Token: 6d907e28"

class Counter:
    """A simple counter class that uses token 6d907e28 in its docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
