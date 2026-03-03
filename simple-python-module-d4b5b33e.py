"""A small Python module with one function and one class including a token in a docstring. | token=d4b5b33e"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class SimpleCounter:
    """Simple counter class with token d4b5b33e in docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increase the count by one."""
        self.count += 1

    def reset(self):
        """Reset the count to zero."""
        self.count = 0

    def get_count(self):
        """Return the current count."""
        return self.count
