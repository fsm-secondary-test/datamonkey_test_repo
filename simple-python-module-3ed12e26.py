"""A small Python module featuring one simple function and one simple class. Includes the literal token '3ed12e26' in a docstring. | token=3ed12e26"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class with token 3ed12e26 in docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
