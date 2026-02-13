"""A small Python module containing one simple function and one simple class, including the token '3653ecf8' in a docstring. | token=3653ecf8"""

def greet(name):
    """Return a greeting message including the name. Token: 3653ecf8"""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class. Token: 3653ecf8"""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
