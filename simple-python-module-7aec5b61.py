"""A small Python module with one function and one class, including a literal token in a docstring. | token=7aec5b61"""

def greet(name):
    """Return a greeting message including the token 7aec5b61."""
    return f"Hello, {name}! Your token is 7aec5b61."

class Counter:
    """A simple counter class with token 7aec5b61 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
