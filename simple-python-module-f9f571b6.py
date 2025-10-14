"""A small Python module containing one function and one class, including a literal token in a docstring. | token=f9f571b6"""

def greet(name):
    """Return a greeting message including the token f9f571b6."""
    return f"Hello, {name}! Token: f9f571b6"

class Counter:
    """Simple counter class that counts up starting from zero.
    Token embedded in docstring: f9f571b6
    """
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
