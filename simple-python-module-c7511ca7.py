"""A Python module with one simple function and one simple class, containing a specific token in the docstring. | token=c7511ca7"""

def greet(name):
    """Return a greeting message including the token c7511ca7."""
    return f"Hello, {name}! This is token c7511ca7."

class Counter:
    """A simple counter class that holds the token c7511ca7 in its docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
