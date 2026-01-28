"""A small Python module containing one simple function and one simple class. The module includes the literal token '37a079ba' in a docstring. | token=37a079ba"""

def greet(name):
    """Return a greeting message for the given name. Token: 37a079ba"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token 37a079ba."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by 1."""
        self.count += 1

    def value(self):
        """Return the current count."""
        return self.count
