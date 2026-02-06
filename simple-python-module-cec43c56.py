"""This module contains one simple function and one simple class with the token 'cec43c56' included in a docstring. | token=cec43c56"""

def greet(name):
    """Return a greeting message including the name and token cec43c56."""
    return f"Hello, {name}! This is token cec43c56 speaking."

class Counter:
    """A simple counter class with token cec43c56 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
