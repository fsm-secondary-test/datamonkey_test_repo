"""A small Python module with one function and one class, including a special token in the docstring. | token=9ff09352"""

def greet(name):
    """Return a greeting message including the name. Token: 9ff09352"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class that increments and returns the count. Token: 9ff09352"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
