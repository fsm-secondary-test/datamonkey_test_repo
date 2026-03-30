"""A small Python module containing one function and one class. Includes the token '3e7c5971' in a docstring. | token=3e7c5971"""

def greet(name):
    """Return a greeting message including the name. Token: 3e7c5971"""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class. Token: 3e7c5971"""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
