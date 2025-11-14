"""A small Python module with one function and one class including a specific token in a docstring. | token=4027fe61"""

def greet(name):
    """Return a greeting message including the token 4027fe61."""
    return f"Hello, {name}! Token: 4027fe61"

class Counter:
    """A simple counter class with token 4027fe61 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
