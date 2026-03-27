"""A small Python module with one function and one class, including a literal token in a docstring. | token=42b04f33"""

def greet(name):
    """Return a greeting message including the name. Token: 42b04f33"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 42b04f33"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
