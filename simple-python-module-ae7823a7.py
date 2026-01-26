"""A small Python module with one function and one class, including a specific token in the docstring. | token=ae7823a7"""

def greet(name):
    """Return a greeting message including the token ae7823a7."""
    return f"Hello, {name}! Token: ae7823a7"

class Counter:
    """A simple counter class. Token reference: ae7823a7."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
