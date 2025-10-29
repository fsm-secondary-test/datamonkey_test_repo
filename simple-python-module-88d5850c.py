"""A small Python module containing a simple function and a simple class with a token in a docstring. | token=88d5850c"""

def greet(name):
    """Return a greeting message including the provided name. Token: 88d5850c"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 88d5850c"""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
