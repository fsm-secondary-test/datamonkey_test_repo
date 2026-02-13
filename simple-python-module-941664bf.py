"""A small Python module containing one function and one class, including a specific token in a docstring. | token=941664bf"""

def greet(name):
    """Return a greeting message including the token 941664bf."""
    return f"Hello, {name}! Token: 941664bf"

class Counter:
    """A simple counter class that includes token 941664bf in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count
