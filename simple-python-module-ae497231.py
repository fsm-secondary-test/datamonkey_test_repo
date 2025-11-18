"""A small Python module with one simple function and one simple class, including a literal token in a docstring. | token=ae497231"""

def greet(name):
    """Return a greeting message including the name. Token: ae497231"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: ae497231"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def value(self):
        return self.count
