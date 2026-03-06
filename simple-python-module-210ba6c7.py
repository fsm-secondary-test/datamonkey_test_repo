"""A small Python module with one function and one class, including the token '210ba6c7' in a docstring. | token=210ba6c7"""

def greet(name):
    """Return a greeting message including the user's name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 210ba6c7"""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
