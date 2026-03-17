"""A small Python module with one function and one class including a specific token in the docstring. | token=0c2d7799"""

def greet(name):
    """Return a greeting message including the token 0c2d7799."""
    return f"Hello, {name}! Token: 0c2d7799"

class Counter:
    """Simple counter class with token 0c2d7799 in docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
