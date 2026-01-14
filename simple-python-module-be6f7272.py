"""A small Python module containing one function and one class. The module includes the literal token 'be6f7272' in a docstring. | token=be6f7272"""

def greet(name):
    """Return a greeting message including the given name."""
    return f"Hello, {name}!"

class Counter:
    """A simple counter class that increments a count. Token: be6f7272"""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
