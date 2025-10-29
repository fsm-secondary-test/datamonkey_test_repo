"""A small Python module containing one function and one class with the literal token '61eaa3dc' in a docstring. | token=61eaa3dc"""

def greet(name):
    """Return a simple greeting message. Token: 61eaa3dc"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 61eaa3dc"""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
        return self.count
