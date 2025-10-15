"""A small Python module with one function and one class including a token in a docstring. | token=3dab85a4"""

def greet(name):
    """Return a greeting message including the token 3dab85a4."""
    return f"Hello, {name}! Token: 3dab85a4"

class Counter:
    """A simple counter class with token 3dab85a4 in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
