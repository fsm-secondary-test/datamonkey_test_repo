"""This module contains a simple function and a simple class with a specific token in the docstring. | token=773ff4a9"""

def greet(name):
    """Return a greeting message including the token '773ff4a9'."""
    return f"Hello, {name}! Token: 773ff4a9"

class Counter:
    """A simple counter class that includes the token '773ff4a9' in its docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
        return self.count
