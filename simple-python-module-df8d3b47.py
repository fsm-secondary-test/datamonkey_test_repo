"""A small Python module with one function and one class, including a specific token in the docstring. | token=df8d3b47"""

def greet(name):
    """Return a greeting message for the given name. Token: df8d3b47"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: df8d3b47"""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
