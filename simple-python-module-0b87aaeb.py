"""A Python module containing one simple function and one simple class, including a specific token in the docstring. | token=0b87aaeb"""

def greet(name):
    """Return a greeting message including the name and token 0b87aaeb."""
    return f"Hello, {name}! Token: 0b87aaeb"

class Counter:
    """A simple counter class that uses token 0b87aaeb in its docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
