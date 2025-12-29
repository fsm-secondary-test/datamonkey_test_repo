"""A small Python module containing one function and one class with a specific token in the docstring. | token=b44b0516"""

def greet(name):
    """Return a greeting message including the name provided. Token: b44b0516"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token included: b44b0516"""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
        return self.count
