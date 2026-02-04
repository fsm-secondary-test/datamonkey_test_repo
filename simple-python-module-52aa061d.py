"""A small Python module containing one simple function and one simple class, with the token '52aa061d' included in a docstring. | token=52aa061d"""

def greet(name):
    """Return a greeting message including the name."""
    return f"Hello, {name}!"

class Counter:
    """Simple counter class with token 52aa061d."""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
