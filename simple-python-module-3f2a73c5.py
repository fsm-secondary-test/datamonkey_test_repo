"""A small Python module with one function and one class, including a specific token in a docstring. | token=3f2a73c5"""

def greet(name):
    """Greet the user by name. Token: 3f2a73c5"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token 3f2a73c5."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count
