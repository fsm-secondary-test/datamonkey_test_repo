"""A small Python module with one simple function and one simple class, including the token '7ef38e6e' in a docstring. | token=7ef38e6e"""

def greet(name):
    """Return a greeting message including the token 7ef38e6e."""
    return f"Hello, {name}! Token: 7ef38e6e"

class Counter:
    """A simple counter class that includes the token 7ef38e6e in its docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
