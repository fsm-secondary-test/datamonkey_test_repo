"""A small Python module with one function and one class, including the token 'd20b3c49' in a docstring. | token=d20b3c49"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: d20b3c49"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
