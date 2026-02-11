"""A Python module with one function and one class, including a specific token in a docstring. | token=35dc2dd1"""

def greet(name):
    """Return a greeting message. Token: 35dc2dd1"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 35dc2dd1"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
