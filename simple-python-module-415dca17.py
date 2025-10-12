"""A small Python module with one function and one class including a specific token in a docstring. | token=415dca17"""

def greet(name):
    """Return a greeting message including the token 415dca17."""
    return f"Hello, {name}! Token: 415dca17"

class Counter:
    """A simple counter class that includes the token 415dca17 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
