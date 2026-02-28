"""A small Python module containing one simple function and one simple class with a specific token in the docstring. | token=0389df3a"""

def greet(name):
    """Return a greeting message including the name. Token: 0389df3a"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 0389df3a"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
