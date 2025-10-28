"""This module contains one simple function and one simple class, including a specific token in the docstring. | token=4afa999c"""

def greet(name):
    """Return a greeting message including the token 4afa999c."""
    return f"Hello, {name}! Token: 4afa999c"

class Counter:
    """A simple counter class that includes token 4afa999c in the docstring."""
    def __init__(self, start=0):
        self.count = start
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
        return self.count
