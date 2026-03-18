"""A small Python module containing one function and one class, including a literal token in a docstring. | token=f15f97ba"""

def greet(name):
    """Return a greeting message including the name. Token: f15f97ba"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token included: f15f97ba"""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
