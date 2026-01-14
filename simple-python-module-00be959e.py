"""A small Python module containing one function and one class, including a specific token in a docstring. | token=00be959e"""

def greet(name):
    """Return a greeting message including the token 00be959e."""
    return f"Hello, {name}! Token: 00be959e"

class Counter:
    """A simple counter class with token 00be959e in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
