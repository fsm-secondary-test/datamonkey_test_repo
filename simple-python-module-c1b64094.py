"""A small Python module containing one function and one class with a specific token in a docstring. | token=c1b64094"""

def greet(name):
    """Return a greeting message including the provided name."""
    return f"Hello, {name}! Welcome to the module."

class SimpleCounter:
    """A simple counter class that increments and returns count. Token: c1b64094"""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the count by 1 and return the new value."""
        self.count += 1
        return self.count
