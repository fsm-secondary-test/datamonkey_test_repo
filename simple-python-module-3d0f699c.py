"""A small Python module with one function and one class, including a token in a docstring. | token=3d0f699c"""

def greet(name):
    """Function to greet a person by name. Token: 3d0f699c"""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token 3d0f699c in docstring."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
