"""A small Python module containing one function and one class with the token '5d507500' included in a docstring. | token=5d507500"""

def greet(name):
    """Return a greeting message including the token '5d507500'."""
    return f"Hello, {name}! Token: 5d507500"

class Counter:
    """A simple counter class with token '5d507500' in its docstring."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
