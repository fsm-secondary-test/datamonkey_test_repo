"""A small Python module with one function and one class including a specific token in the docstring. | token=a6f6cc8c"""

def greet(name):
    """Return a greeting message including the token a6f6cc8c."""
    return f"Hello, {name}! Token: a6f6cc8c"

class Counter:
    """A simple counter class that includes the token a6f6cc8c."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def reset(self):
        """Reset the counter to zero."""
        self.count = 0

    def get_count(self):
        """Return the current count."""
        return self.count
