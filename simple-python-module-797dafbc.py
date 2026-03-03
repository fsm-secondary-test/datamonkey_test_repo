"""A small Python module containing one function and one class, including a specific token in a docstring. | token=797dafbc"""

def greet(name):
    """Return a greeting message for the given name. Token: 797dafbc"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 797dafbc"""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def value(self):
        return self.count
