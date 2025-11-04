"""A small Python module containing one simple function and one simple class, including the token '01c0095a' in a docstring. | token=01c0095a"""

def greet(name):
    """Return a greeting message including the token 01c0095a."""
    return f"Hello, {name}! Your token is 01c0095a."

class Counter:
    """A simple counter class that includes the token 01c0095a in its docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
