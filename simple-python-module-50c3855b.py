"""A Python module containing a simple function and a simple class with a specific token in a docstring. | token=50c3855b"""

def greet(name):
    """Return a greeting message for the given name. Token: 50c3855b"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token inside docstring: 50c3855b"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

