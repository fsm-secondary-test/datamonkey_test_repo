"""A small Python module containing one simple function and one simple class with a specific token in the docstring. | token=a1a34983"""

def greet(name):
    """Return a greeting message including the token a1a34983."""
    return f"Hello, {name}! Welcome to the a1a34983 module."

class Counter:
    """Simple counter class with token a1a34983 in docstring."""

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
