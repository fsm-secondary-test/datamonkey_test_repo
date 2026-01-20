"""A small Python module with one function and one class, including a special token in the docstring. | token=d35f5bb1"""

def greet(name):
    """Return a greeting message including the name. Token: d35f5bb1"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: d35f5bb1"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count
