"""A small Python module containing one function and one class, including a specific token in a docstring. | token=3c40fe8d"""

def greet(name):
    """Return a greeting message including the token 3c40fe8d."""
    return f"Hello, {name}! Token: 3c40fe8d"

class Counter:
    """Simple counter class that internally uses the token '3c40fe8d' in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
