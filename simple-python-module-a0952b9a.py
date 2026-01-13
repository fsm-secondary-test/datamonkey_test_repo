"""This module contains one simple function and one simple class with a specific token in the docstring. | token=a0952b9a"""

def greet(name):
    """Return a greeting message including the given name. Token: a0952b9a"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: a0952b9a"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
