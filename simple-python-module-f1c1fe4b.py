"""A small Python module with one function and one class, including a specific token in the docstring. | token=f1c1fe4b"""

def greet(name):
    """Return a greeting message including the provided name. Token: f1c1fe4b"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: f1c1fe4b"""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
