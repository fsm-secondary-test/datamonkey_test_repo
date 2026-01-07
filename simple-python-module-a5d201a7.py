"""A small Python module containing one function and one class, including a specific token in a docstring. | token=a5d201a7"""

def greet(name):
    """Return a greeting message including the token a5d201a7."""
    return f"Hello, {name}! Token: a5d201a7"

class Counter:
    """Simple counter class with token a5d201a7 in the docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
