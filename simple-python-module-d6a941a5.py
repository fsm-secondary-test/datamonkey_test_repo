"""A small Python module with one function and one class, including a specific token in the docstring. | token=d6a941a5"""

def greet(name):
    """Return a greeting message for the given name. Token: d6a941a5"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: d6a941a5"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
