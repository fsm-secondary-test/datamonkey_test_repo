"""A small Python module with one function and one class, including a literal token in a docstring. | token=a3419eda"""

def greet(name):
    """Return a greeting message for the given name. Token: a3419eda"""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class. Token: a3419eda"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def value(self):
        return self.count
