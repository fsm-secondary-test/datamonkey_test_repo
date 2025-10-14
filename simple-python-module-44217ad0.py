"""A small Python module containing one function and one class with a specific token in docstrings. | token=44217ad0"""

def greet(name):
    """Return a greeting message with the given name. Token: 44217ad0"""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class. Token: 44217ad0"""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
        return self.count
