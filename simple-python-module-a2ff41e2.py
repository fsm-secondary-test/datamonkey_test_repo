"""This module contains a simple function and a simple class with the token 'a2ff41e2' included in a docstring. | token=a2ff41e2"""

def greet(name):
    """Return a greeting message including the name and token a2ff41e2."""
    return f"Hello, {name}! Token: a2ff41e2"

class Counter:
    """Simple counter class that includes the token a2ff41e2 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        """Increment the counter by one."""
        self.count += 1

    def value(self):
        """Return the current count value."""
        return self.count
