"""A small Python module with one function and one class including a specific token in a docstring. | token=0eb29903"""

def greet(name):
    """Return a greeting message including the token 0eb29903."""
    return f"Hello, {name}! Token: 0eb29903"

class Counter:
    """A simple counter class including token 0eb29903 in docstring."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
