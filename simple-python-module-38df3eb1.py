"""This module contains a simple function and a simple class with the token '38df3eb1' in the docstring. | token=38df3eb1"""

def greet(name):
    """Returns a greeting message including the name and token 38df3eb1."""
    return f"Hello, {name}! Your token is 38df3eb1."

class Counter:
    """A simple counter class that counts upwards starting at zero. Token: 38df3eb1."""

    def __init__(self):
        self.count = 0

    def increment(self):
        """Increase the counter by one."""
        self.count += 1

    def value(self):
        """Return the current count value."""
        return self.count
