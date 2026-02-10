"""A small Python module containing one function and one class, with a specific token in the docstring. | token=1a7f1559"""

def greet(name):
    """Return a greeting message for the given name. Token: 1a7f1559"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 1a7f1559"""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
