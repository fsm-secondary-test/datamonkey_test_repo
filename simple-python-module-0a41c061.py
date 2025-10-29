"""A small Python module with one function and one class, including a specific token in a docstring. | token=0a41c061"""

def greet(name):
    """Return a greeting message including the given name. Token: 0a41c061"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 0a41c061"""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count
