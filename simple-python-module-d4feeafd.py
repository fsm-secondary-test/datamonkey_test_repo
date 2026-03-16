"""A small Python module with one function and one class, including a specific token in docstrings. | token=d4feeafd"""

def greet(name):
    """Return a greeting message including the token d4feeafd."""
    return f"Hello, {name}! Token: d4feeafd"

class Counter:
    """A simple counter class that uses token d4feeafd in its docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
