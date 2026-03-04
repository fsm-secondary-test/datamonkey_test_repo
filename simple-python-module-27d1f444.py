"""A Python module containing one simple function and one simple class. Includes the token '27d1f444' in a docstring. | token=27d1f444"""

def greet(name):
    """Return a greeting message including the token '27d1f444'."""
    return f"Hello, {name}! Token: 27d1f444"

class Counter:
    """A simple counter class with token '27d1f444' included in the docstring."""
    def __init__(self, start=0):
        self.count = start
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
