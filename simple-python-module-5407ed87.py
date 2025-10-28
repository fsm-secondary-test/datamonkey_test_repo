"""A small Python module with one function and one class, including a literal token in a docstring. | token=5407ed87"""

def greet(name):
    """Return a greeting message including the token 5407ed87."""
    return f"Hello, {name}! Your token is 5407ed87."

class Counter:
    """A simple counter class with token 5407ed87 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def value(self):
        return self.count
