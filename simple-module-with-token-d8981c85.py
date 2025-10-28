"""A small Python module containing one function and one class, including a specific token in the docstring. | token=d8981c85"""

def greet(name):
    """Return a greeting message including the token d8981c85."""
    return f"Hello, {name}! Token: d8981c85"

class Counter:
    """Simple counter class including token d8981c85 in docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the count by one."""
        self.count += 1

    def reset(self):
        """Reset the count to zero."""
        self.count = 0

    def get_count(self):
        """Get the current count value."""
        return self.count
