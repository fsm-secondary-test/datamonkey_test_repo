"""A small Python module with one function and one class including a specific token in docstrings. | token=c9338252"""

def greet(name):
    """Return a greeting message including the token c9338252."""
    return f"Hello, {name}! Token c9338252 included."

class Counter:
    """A simple counter class with token c9338252 in the docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def reset(self):
        """Reset the counter to zero."""
        self.count = 0

    def get_count(self):
        """Get the current count."""
        return self.count
