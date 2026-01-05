"""A small Python module with one function and one class including a specific token in a docstring. | token=c21bf0a0"""

def greet(name):
    """Return a greeting message including the token c21bf0a0."""
    return f"Hello, {name}! Token: c21bf0a0"

class Counter:
    """Simple counter class with token c21bf0a0 in docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
