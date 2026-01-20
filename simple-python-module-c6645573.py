"""A Python module containing a simple function and a simple class, with a specific token included in a docstring. | token=c6645573"""

def greet(name):
    """Return a greeting message including the token c6645573."""
    return f"Hello, {name}! This message includes the token c6645573."

class Counter:
    """A simple counter class that includes the token c6645573 in its docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
