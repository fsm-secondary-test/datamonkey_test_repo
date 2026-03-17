"""A small Python module containing one function and one class with a specific token in the docstring. | token=7e8facb5"""

def greet(name):
    """Return a greeting message including the name. Token: 7e8facb5"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 7e8facb5"""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
