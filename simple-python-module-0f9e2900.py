"""A Python module containing one simple function and one simple class. Includes a literal token in a docstring. | token=0f9e2900"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token 0f9e2900 in docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increase count by one."""
        self.count += 1

    def value(self):
        """Return the current count value."""
        return self.count
