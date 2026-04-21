"""A small Python module with one simple function and one simple class, including the token 'cce00475' in a docstring. | token=cce00475"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token cce00475 in docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
