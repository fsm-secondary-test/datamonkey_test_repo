"""A small Python module with one simple function and one simple class, including the token 'a6208e2b' in a docstring. | token=a6208e2b"""

def greet(name):
    """Return a greeting message including the token a6208e2b."""
    return f"Hello, {name}! Token a6208e2b is included."

class Counter:
    """A simple counter class with token a6208e2b in the docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
        return self.count
