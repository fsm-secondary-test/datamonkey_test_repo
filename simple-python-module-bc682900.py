"""A small Python module containing one simple function and one simple class, including a specific token in a docstring. | token=bc682900"""

def greet(name):
    """Return a greeting message including the given name and token bc682900."""
    return f"Hello, {name}! Token: bc682900"

class Counter:
    """A simple counter class with token bc682900 in the docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count

    def reset(self):
        self.count = 0
