"""A small Python module containing one function and one class with a specific token in the docstring. | token=f9f571b6"""

def greet(name):
    """Return a greeting message including the provided name. Token: f9f571b6"""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class. Token: f9f571b6"""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def value(self):
        return self.count
