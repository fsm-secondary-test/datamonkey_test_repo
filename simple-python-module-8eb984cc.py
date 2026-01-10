"""A small Python module with one function and one class, including a token in the docstring. | token=8eb984cc"""

def greet(name):
    """Return a greeting message including the token 8eb984cc."""
    return f"Hello, {name}! Your token is 8eb984cc."

class Counter:
    """A simple counter class that includes the token 8eb984cc."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
