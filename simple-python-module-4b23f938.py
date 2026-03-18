"""A small Python module containing one simple function and one simple class. Includes the literal token '4b23f938' in a docstring. | token=4b23f938"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 4b23f938"""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
