"""A small Python module containing one simple function and one simple class, including the token '810a0fbd' in a docstring. | token=810a0fbd"""

def greet(name):
    """Return a greeting message including the name. Token: 810a0fbd"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 810a0fbd"""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
