"""This module contains a simple function and a simple class, including a specific token in the docstring. | token=2571b90b"""

def greet(name):
    """Return a greeting message including the token 2571b90b."""
    return f"Hello, {name}! This is token 2571b90b."

class Counter:
    """A simple counter class that uses the token 2571b90b in its docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
        return self.count
