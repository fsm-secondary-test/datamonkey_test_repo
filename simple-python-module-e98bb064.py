"""A small Python module with one function and one class, including a specific token in a docstring. | token=e98bb064"""

def greet(name):
    """Return a greeting message including the token e98bb064."""
    return f"Hello, {name}! Token: e98bb064"

class Counter:
    """A simple counter class with token e98bb064 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
