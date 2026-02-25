"""A small Python module containing one simple function and one simple class. Includes the token '6620e8a1' in a docstring. | token=6620e8a1"""

def greet(name):
    """Return a greeting message including the token 6620e8a1."""
    return f"Hello, {name}! Your token is 6620e8a1."

class Counter:
    """A simple counter class that uses token 6620e8a1 in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
