"""A simple Python module with one function and one class, including a specific token in a docstring. | token=49a6767b"""

def greet(name):
    """Return a greeting message including the name. Token: 49a6767b"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 49a6767b"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0
