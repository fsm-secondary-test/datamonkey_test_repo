"""This module contains a simple function and a simple class, including the token '55c3a8b3' in a docstring. | token=55c3a8b3"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class SimpleCounter:
    """A simple counter class that includes the token 55c3a8b3 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def get_count(self):
        """Return the current count."""
        return self.count
