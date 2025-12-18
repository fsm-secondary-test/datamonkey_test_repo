"""A Python module containing one function and one class, including a literal token in the docstring. | token=e22a8afb"""

def greet(name):
    """Return a greeting message for the given name. Token: e22a8afb"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: e22a8afb"""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
