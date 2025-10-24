"""A small Python module with one simple function and one simple class, including a literal token in a docstring. | token=5db1b0d4"""

def greet(name):
    """Return a simple greeting message including the token '5db1b0d4'."""
    return f"Hello, {name}! Token: 5db1b0d4"

class Counter:
    """A simple counter class with token '5db1b0d4' in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count

