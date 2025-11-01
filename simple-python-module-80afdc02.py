"""A small Python module containing one simple function and one simple class, including the token '80afdc02' in a docstring. | token=80afdc02"""

def greet(name):
    """Return a greeting message including the token 80afdc02."""
    return f"Hello, {name}! Your token is 80afdc02."

class Counter:
    """A simple counter class that counts up from zero. Token: 80afdc02."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
