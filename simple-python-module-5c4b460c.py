"""A small Python module containing one function and one class with a specific token in the docstring. | token=5c4b460c"""

def greet(name):
    """Return a greeting message including the token 5c4b460c."""
    return f"Hello, {name}! Token: 5c4b460c"

class Counter:
    """A simple counter class that includes the token 5c4b460c in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
