"""A small Python module with one function and one class, including a specific token in the docstring. | token=7c8cf4ac"""

def greet(name):
    """Return a greeting message including the token 7c8cf4ac."""
    return f"Hello, {name}! Your token is 7c8cf4ac."

class Counter:
    """A simple counter class with token 7c8cf4ac in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
