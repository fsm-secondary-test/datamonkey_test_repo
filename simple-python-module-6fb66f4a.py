"""A small Python module with one function and one class, including a specific token in a docstring. | token=6fb66f4a"""

def greet(name):
    """Return a greeting message including the token 6fb66f4a."""
    return f"Hello, {name}! Token: 6fb66f4a"

class Counter:
    """A simple counter class that includes the token 6fb66f4a in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
