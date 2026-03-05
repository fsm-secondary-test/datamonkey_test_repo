"""A small Python module containing one function and one class with the token '34f5d046' included in a docstring. | token=34f5d046"""

def greet(name):
    """Return a greeting message including the provided name. Token: 34f5d046"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 34f5d046"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
